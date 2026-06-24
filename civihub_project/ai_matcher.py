"""
Primus 1 — CiviHub AI Engine
- Job Matching (skill match + TF-IDF + experience + location)
- Professional Grading (project quality, skill breadth, experience, profile, community)
- Career Assistant (rule-based smart responses)
"""

import re
import math

# ---------- CIVIL ENGINEERING SKILL KEYWORDS ----------

CIVIL_SKILLS = {
    "autocad", "revit", "staad pro", "staad", "etabs", "sap2000",
    "primavera", "ms project", "matlab", "gis", "arcgis", "qgis",
    "bim", "civil 3d", "tekla", "navisworks", "bluebeam",
    "concrete", "structural analysis", "foundation", "geotechnical",
    "soil mechanics", "surveying", "leveling", "total station",
    "rcc", "steel", "prestressed", "post-tensioned",
    "highway", "bridge", "tunnel", "dam", "water treatment",
    "hydrology", "hydraulics", "environmental", "construction management",
    "estimation", "costing", "quantity surveying", "billing",
    "site supervision", "quality control", "safety", "planning",
    "scheduling", "project management", "lean construction",
    "python", "excel", "solidworks", "sketchup", "lumion",
}


# ================================================================
# 1. JOB MATCHING
# ================================================================

def _normalize(text):
    """Lowercase and strip punctuation for matching."""
    if not text:
        return ""
    return re.sub(r"[^a-z0-9\s]", "", text.lower()).strip()


def _extract_skills(text):
    """Split comma/semicolon separated skills into a clean set."""
    if not text:
        return set()
    parts = re.split(r"[,;|/]+", text.lower())
    return {p.strip() for p in parts if p.strip()}


def _skill_match_score(user_skills, job_skills):
    """Fraction of job skills matched by user."""
    if not job_skills:
        return 0.5  # neutral if job doesn't specify
    matched = user_skills & job_skills
    return len(matched) / len(job_skills) if job_skills else 0


def _text_similarity(text_a, text_b):
    """
    Simple TF-based cosine similarity (no sklearn dependency needed at runtime).
    Falls back gracefully.
    """
    if not text_a or not text_b:
        return 0.0

    words_a = _normalize(text_a).split()
    words_b = _normalize(text_b).split()

    if not words_a or not words_b:
        return 0.0

    # Build term frequency vectors
    all_words = set(words_a) | set(words_b)
    vec_a = {w: words_a.count(w) for w in all_words}
    vec_b = {w: words_b.count(w) for w in all_words}

    # Cosine similarity
    dot = sum(vec_a[w] * vec_b[w] for w in all_words)
    mag_a = math.sqrt(sum(v ** 2 for v in vec_a.values()))
    mag_b = math.sqrt(sum(v ** 2 for v in vec_b.values()))

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return dot / (mag_a * mag_b)


def _experience_score(user_exp, job_title):
    """Score experience alignment based on job title seniority cues."""
    try:
        years = float(user_exp)
    except (TypeError, ValueError):
        years = 0

    title_lower = (job_title or "").lower()

    # Infer expected level
    if any(kw in title_lower for kw in ["senior", "lead", "principal", "head", "manager", "director"]):
        expected = 7
    elif any(kw in title_lower for kw in ["mid", "intermediate"]):
        expected = 3
    elif any(kw in title_lower for kw in ["junior", "intern", "trainee", "entry", "fresher"]):
        expected = 0.5
    else:
        expected = 3  # default mid

    # Score: close to expected is best
    diff = abs(years - expected)
    if diff <= 1:
        return 1.0
    elif diff <= 3:
        return 0.7
    elif diff <= 5:
        return 0.4
    else:
        return 0.2


def _location_score(user_location, job_location):
    """Simple substring matching for location."""
    if not user_location or not job_location:
        return 0.3  # neutral
    u = _normalize(user_location)
    j = _normalize(job_location)
    if u in j or j in u:
        return 1.0
    # Check city-level overlap
    u_parts = set(u.split())
    j_parts = set(j.split())
    overlap = u_parts & j_parts
    if overlap:
        return 0.7
    return 0.1


def score_jobs(user, jobs):
    """
    Score all jobs for a user. Returns list of dicts:
    [{ "job": <job_row>, "score": 0-100, "matched_skills": [...], "tips": "..." }, ...]
    """
    user_skills = _extract_skills(user.get("skills", ""))
    user_text = " ".join(filter(None, [
        user.get("skills", ""),
        user.get("qualifications", ""),
        user.get("portfolio", ""),
    ]))

    results = []

    for job in jobs:
        job_skills = _extract_skills(job.get("skills_required", ""))
        job_text = " ".join(filter(None, [
            job.get("job_title", ""),
            job.get("job_description", ""),
            job.get("skills_required", ""),
        ]))

        # 4-factor scoring
        s_skill = _skill_match_score(user_skills, job_skills)
        s_text = _text_similarity(user_text, job_text)
        s_exp = _experience_score(user.get("experience"), job.get("job_title", ""))
        s_loc = _location_score(user.get("location"), job.get("location", ""))

        score = (s_skill * 0.50) + (s_text * 0.30) + (s_exp * 0.10) + (s_loc * 0.10)
        score_pct = min(round(score * 100), 99)  # cap at 99

        matched = list(user_skills & job_skills)
        missing = list(job_skills - user_skills)

        tip = ""
        if missing:
            tip = f"Learn {', '.join(missing[:3])} to boost your match."

        results.append({
            "job": job,
            "score": score_pct,
            "matched_skills": matched,
            "missing_skills": missing,
            "tip": tip,
            "breakdown": {
                "skill": round(s_skill * 100),
                "relevance": round(s_text * 100),
                "experience": round(s_exp * 100),
                "location": round(s_loc * 100),
            }
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results


# ================================================================
# 2. PROFESSIONAL GRADING
# ================================================================

def grade_user(user, projects, post_count=0, msg_count=0):
    """
    Grade a user on 5 criteria. Returns:
    {
        "letter": "A",
        "label": "Senior Expert",
        "color": "#3b82f6",
        "score": 82,
        "criteria": { ... },
        "tips": [ ... ]
    }
    """
    tips = []

    # --- Project Quality (30%) ---
    num_projects = len(projects) if projects else 0
    project_detail_score = 0

    if num_projects > 0:
        for p in projects:
            desc = p.get("project_description", "") or ""
            link = p.get("project_link", "") or ""
            # Points: description length + has link
            d_score = min(len(desc) / 200, 1.0)  # max at 200 chars
            l_score = 1.0 if link.strip() else 0.0
            project_detail_score += (d_score * 0.6 + l_score * 0.4)

        project_detail_avg = project_detail_score / num_projects
    else:
        project_detail_avg = 0

    # Quantity score: 0 projects = 0, 5+ = 1.0
    quantity_score = min(num_projects / 5, 1.0)
    s_project = (quantity_score * 0.5 + project_detail_avg * 0.5)

    if num_projects == 0:
        tips.append("Add your first project to start building your grade.")
    elif num_projects < 3:
        tips.append(f"Add {3 - num_projects} more project(s) to strengthen your portfolio.")
    if num_projects > 0 and project_detail_avg < 0.5:
        tips.append("Add detailed descriptions and links to your projects for a higher score.")

    # --- Skill Breadth (25%) ---
    user_skills = _extract_skills(user.get("skills", ""))
    num_skills = len(user_skills)
    # Civil relevance bonus
    civil_overlap = user_skills & CIVIL_SKILLS
    relevance = len(civil_overlap) / max(num_skills, 1)

    quantity_s = min(num_skills / 8, 1.0)  # 8+ skills = max
    s_skills = (quantity_s * 0.6 + relevance * 0.4)

    if num_skills < 4:
        tips.append(f"Add more skills — try AutoCAD, Revit, STAAD Pro, or Primavera.")
    if relevance < 0.3 and num_skills > 0:
        tips.append("Add more civil engineering-specific skills to boost relevance.")

    # --- Experience Depth (20%) ---
    try:
        years = float(user.get("experience", 0) or 0)
    except (TypeError, ValueError):
        years = 0

    if years >= 10:
        s_exp = 1.0
    elif years >= 5:
        s_exp = 0.8
    elif years >= 2:
        s_exp = 0.6
    elif years >= 1:
        s_exp = 0.4
    else:
        s_exp = 0.15

    if years < 2:
        tips.append("Gain more hands-on experience through internships or freelance work.")

    # --- Profile Completeness (15%) ---
    fields = ["username", "email", "phone", "location", "skills", "qualifications",
              "experience", "portfolio", "profile_image", "resume"]
    filled = sum(1 for f in fields if user.get(f) and str(user.get(f, "")).strip())
    s_profile = filled / len(fields)

    missing_fields = [f for f in fields if not user.get(f) or not str(user.get(f, "")).strip()]
    if missing_fields:
        readable = ", ".join(missing_fields[:3]).replace("_", " ").title()
        tips.append(f"Complete your profile — fill in: {readable}.")

    # --- Community Engagement (10%) ---
    engagement = min((post_count * 2 + msg_count) / 20, 1.0)
    s_community = engagement

    if post_count == 0:
        tips.append("Post your first project update on the dashboard to boost engagement.")
    if msg_count == 0:
        tips.append("Start chatting with other professionals to grow your network.")

    # --- FINAL SCORE ---
    total = (
        s_project * 30 +
        s_skills * 25 +
        s_exp * 20 +
        s_profile * 15 +
        s_community * 10
    )
    total = round(total)

    # Letter grade
    if total >= 90:
        letter, label, color = "S", "Elite Professional", "#9333ea"
    elif total >= 75:
        letter, label, color = "A", "Senior Expert", "#3b82f6"
    elif total >= 60:
        letter, label, color = "B", "Skilled Professional", "#22c55e"
    elif total >= 45:
        letter, label, color = "C", "Growing Engineer", "#eab308"
    else:
        letter, label, color = "D", "Beginner", "#f97316"

    return {
        "letter": letter,
        "label": label,
        "color": color,
        "score": total,
        "criteria": {
            "project_quality": round(s_project * 100),
            "skill_breadth": round(s_skills * 100),
            "experience_depth": round(s_exp * 100),
            "profile_completeness": round(s_profile * 100),
            "community_engagement": round(s_community * 100),
        },
        "tips": tips[:5],  # max 5 tips
    }


# ================================================================
# 3. CONTINUOUS LEARNING
# ================================================================

def learn_platform_skills(all_users, all_projects, all_messages):
    """
    Analyzes all users on the platform, grades them, and extracts the most common
    skills used by Grade S and Grade A professionals.
    """
    top_tier_skills = {}
    
    for u in all_users:
        # Filter data for this user
        u_projects = [p for p in all_projects if p.get('user_id') == u.get('id')]
        post_count = len(u_projects)
        msg_count = len([m for m in all_messages if m.get('sender_id') == u.get('id')])
        
        # Grade the user
        g_info = grade_user(u, u_projects, post_count, msg_count)
        
        # If they are top tier, extract their skills
        if g_info['letter'] in ['S', 'A']:
            u_skills = _extract_skills(u.get('skills', ''))
            for s in u_skills:
                # S-tier skills get slightly more weight
                weight = 2 if g_info['letter'] == 'S' else 1
                top_tier_skills[s] = top_tier_skills.get(s, 0) + weight

    return top_tier_skills


def learn_conversation_trends(recent_qs):
    """
    Analyzes recent AI questions to find trending topics.
    """
    trends = {}
    keywords = ["salary", "skills", "improve", "grade", "job", "recommendation", "portfolio", "resume", "interview", "certification", "autocad", "revit"]
    
    for row in recent_qs:
        q_lower = row['question'].lower()
        for kw in keywords:
            if kw in q_lower:
                trends[kw] = trends.get(kw, 0) + 1
                
    sorted_trends = sorted(trends.items(), key=lambda item: item[1], reverse=True)
    return [t[0] for t in sorted_trends[:3]]


# ================================================================
# 4. CAREER ASSISTANT
# ================================================================

def get_career_advice(user, jobs, grade_info, question, learning_context=None):
    """
    Primus 1 — deeply tailored career assistant.
    Every response uses the user's actual profile data.
    """
    q = question.lower().strip()
    name = user.get("username", "there").split()[0]  # first name
    user_skills = _extract_skills(user.get("skills") or "")
    skills_str = ", ".join(sorted(user_skills)[:6]) if user_skills else "none listed"
    location = (user.get("location") or "").strip() or "an unspecified location"
    qualifications = (user.get("qualifications") or "").strip() or "not specified"
    portfolio = (user.get("portfolio") or "").strip()

    try:
        years = float(user.get("experience", 0) or 0)
    except (TypeError, ValueError):
        years = 0

    grade = grade_info.get("letter", "?")
    score = grade_info.get("score", 0)
    tips = grade_info.get("tips", [])
    criteria = grade_info.get("criteria", {})

    # Execute Learning Context
    top_platform_skills = {}
    trending_topics = []
    
    if learning_context:
        top_platform_skills = learn_platform_skills(
            learning_context.get("all_users", []),
            learning_context.get("all_projects", []),
            learning_context.get("all_messages", [])
        )
        trending_topics = learn_conversation_trends(learning_context.get("recent_qs", []))

    # Weakest criterion
    weakest_key = min(criteria, key=criteria.get) if criteria else None
    weakest_names = {
        "project_quality": "Project Quality",
        "skill_breadth": "Skill Breadth",
        "experience_depth": "Experience Depth",
        "profile_completeness": "Profile Completeness",
        "community_engagement": "Community Engagement",
    }
    weakest_name = weakest_names.get(weakest_key, "")
    weakest_score = criteria.get(weakest_key, 0)

    # Strongest criterion
    strongest_key = max(criteria, key=criteria.get) if criteria else None
    strongest_name = weakest_names.get(strongest_key, "")
    strongest_score = criteria.get(strongest_key, 0)

    # Project stats
    scored_jobs = score_jobs(user, jobs)
    num_jobs = len(scored_jobs)
    top_job = scored_jobs[0] if scored_jobs else None

    # --- Intent detection ---

    # Best job / recommendation
    if any(kw in q for kw in ["best job", "which job", "recommend", "suited", "suit me", "match", "find job", "suggest"]):
        if top_job:
            j = top_job["job"]
            matched = ", ".join(top_job["matched_skills"][:5]) or "general civil engineering"
            missing = ", ".join(top_job["missing_skills"][:3])

            resp = (
                f"Hey {name}, based on your skills in {skills_str} and "
                f"your {years:.0f} years of experience in {location}, "
                f"the best match I found is for a {j.get('job_title')} position at {j.get('company_name')}. "
                f"This is a {top_job['score']}% match for you. "
            )
            if j.get("salary_range"):
                resp += f"The salary range for this role is {j.get('salary_range')}. "

            resp += f"Your skills in {matched} match perfectly with what they are looking for."

            if missing:
                resp += f" However, you might want to brush up on {missing} to improve your chances."

            if num_jobs > 1:
                second = scored_jobs[1]
                resp += (
                    f" Another great option is the {second['job']['job_title']} role at "
                    f"{second['job']['company_name']}, which is a {second['score']}% match."
                )

            if top_job.get("tip"):
                resp += f" My advice: {top_job['tip']}"

            return resp
        return f"{name}, there are no jobs posted on CiviHub right now. I will let you know as soon as new positions drop that match your skills in {skills_str}."

    # Improve / grade
    if any(kw in q for kw in ["improve", "grade", "better", "boost", "upgrade", "increase", "how can i", "level up"]):
        resp = (
            f"You are currently at Grade {grade} with a score of {score} out of 100, {name}. "
            f"Looking at your breakdown, your strongest area is {strongest_name} at {strongest_score}%. "
            f"However, your weakest area is {weakest_name} at {weakest_score}%, which is holding you back. "
        )

        if tips:
            resp += "Here is my personalized action plan for you: "
            resp += " ".join(tips)

            next_thresholds = {"D": ("C", 45), "C": ("B", 60), "B": ("A", 75), "A": ("S", 90)}
            if grade in next_thresholds:
                next_letter, next_score = next_thresholds[grade]
                gap = next_score - score
                resp += f" You just need {gap} more points to reach Grade {next_letter}. I recommend focusing on {weakest_name} first to close that gap quickly."

        return resp

    # Skills
    if any(kw in q for kw in ["skill", "learn", "technology", "tool", "software"]):
        missing = CIVIL_SKILLS - user_skills
        
        # CONTINUOUS LEARNING: Dynamic Skill Recommendation
        if top_platform_skills:
            learned_missing = {k: v for k, v in top_platform_skills.items() if k not in user_skills}
            top_missing = sorted(learned_missing.keys(), key=lambda x: -learned_missing[x])[:6]
        else:
            job_skill_freq = {}
            for job in jobs:
                for s in _extract_skills(job.get("skills_required", "")):
                    if s in missing:
                        job_skill_freq[s] = job_skill_freq.get(s, 0) + 1
            top_missing = sorted(job_skill_freq.keys(), key=lambda x: -job_skill_freq[x])[:6]

            if not top_missing:
                top_missing = sorted(list(missing))[:6]

        resp = (
            f"{name}, you currently have {len(user_skills)} skills listed on your profile, including {skills_str}. "
            f"Your overall Skill Breadth score is {criteria.get('skill_breadth', 0)}%. "
        )

        if top_missing:
            top_missing_str = ", ".join(top_missing[:3])
            if top_platform_skills:
                resp += f"I have analyzed all Grade S and Grade A professionals on CiviHub, and I noticed you are missing {top_missing_str}. These are in very high demand among top-tier peers. "
            else:
                resp += f"Based on current job listings, the most in-demand skills you are missing are {top_missing_str}. "

            resp += f"Adding just a few of these to your repertoire would boost your Skill Breadth significantly and open up more job opportunities."
        else:
            resp += "Your skillset covers all major civil engineering tools. You are definitely ahead of the curve."

        return resp

    # Salary
    if any(kw in q for kw in ["salary", "pay", "compensation", "earning", "money", "package"]):
        jobs_with_salary = [j for j in jobs if j.get("salary_range")]
        resp = (
            f"With your {years:.0f} years of experience in {location} and your skills in {skills_str}, "
            f"you are currently a Grade {grade} professional. "
        )

        if jobs_with_salary and top_job:
            salary_examples = []
            for sj in scored_jobs[:2]:
                if sj["job"].get("salary_range"):
                    salary_examples.append(f"{sj['job']['salary_range']} for a {sj['job']['job_title']} role")
            if salary_examples:
                resp += f"Looking at matching jobs, you could expect around {' and '.join(salary_examples)}. "

        if years < 3:
            resp += "At your experience level, focusing on building a strong portfolio will directly impact your future negotiation power."
        elif years < 7:
            resp += "You have enough experience to negotiate confidently. You should consider stepping into leadership roles for a significant salary jump."
        else:
            resp += "With your seniority, you are well-positioned for principal or lead roles, and your grade gives you strong credibility with recruiters."

        return resp

    # Experience
    if any(kw in q for kw in ["experience", "internship", "fresher", "entry level", "career path"]):
        resp = f"You have {years:.0f} years of experience, {name}. "

        if years < 1:
            resp += (
                "Since you are just getting started, your best roadmap is to get certified in tools like AutoCAD or Revit, "
                "chase internships even for a few months, and build your portfolio on CiviHub by posting academic projects. "
                f"Your Experience Depth score is currently {criteria.get('experience_depth', 0)}%, but every month of real work will raise this."
            )
        elif years < 4:
            resp += (
                "You are in a crucial growth phase. Your skills are solid, so it's time to specialize in one area. "
                "Try to lead a small team or sub-project to build management credibility. Getting a PMP certification would be a great accelerator for you. "
                f"Your Experience Depth score is {criteria.get('experience_depth', 0)}%, which shows you are right on track."
            )
        else:
            resp += (
                f"That is a strong amount of experience. As a Grade {grade} professional, your next moves should be to "
                "mentor junior engineers on CiviHub to boost your community engagement score, and maybe consider freelance consulting for premium rates. "
                "You already command respect, so just fill any remaining gaps in your profile to reach the top tier."
            )

        return resp

    # Profile
    if any(kw in q for kw in ["profile", "resume", "portfolio", "complete"]):
        completeness = criteria.get("profile_completeness", 0)

        fields_check = {
            "phone": user.get("phone"),
            "location": user.get("location"),
            "skills": user.get("skills"),
            "qualifications": user.get("qualifications"),
            "experience": user.get("experience"),
            "portfolio": user.get("portfolio"),
            "profile_image": user.get("profile_image"),
            "resume": user.get("resume"),
        }
        missing = [k.replace("_", " ").title() for k, v in fields_check.items() if not v or not str(v).strip()]

        resp = f"{name}, your profile is {completeness}% complete. "

        if missing:
            resp += f"You are currently missing your {', '.join(missing)}. "
            resp += "Completing these fields would bring you closer to 100%, and fully complete profiles get significantly more visibility from recruiters."
        else:
            resp += "All fields are filled out, so your profile is fully complete and looking great."

        if not portfolio:
            resp += " As a pro tip, make sure to add a portfolio link like a personal website or Behance page, as it's the number one thing recruiters check."

        return resp

    # Hello / greeting
    if any(kw in q for kw in ["hello", "hi", "hey", "help", "what can you", "who are you", "primus"]):
        resp = (
            f"Hey {name}, I am Primus 1, your CiviHub AI career engine. "
            f"I already have your profile loaded up. I see you have {years:.0f} years of experience in {location}, "
            f"and you're currently a Grade {grade} professional with a score of {score} out of 100. "
            f"I also analyzed {len(scored_jobs)} jobs against your skills in {skills_str}. "
        )
        
        if trending_topics:
            resp += f"Right now, a lot of professionals on CiviHub are asking me about {', '.join(trending_topics)}. "
            
        resp += (
            "You can ask me anything specific. For example, you can ask me which job suits you best, "
            "how to improve your grade, what skills you are missing compared to top-graded peers, "
            "or what kind of salary you can expect based on your experience."
        )
        return resp

    # Default — still personalized
    return (
        f"I hear you asking about '{question}', {name}. "
        f"Based on what I know about you, you are a Grade {grade} professional with {years:.0f} years of experience in {location}. "
        f"I can give you deep, personalized answers if you ask me things like which job suits you best, how to improve your grade, "
        f"what skills you should learn, or what your salary potential is. How can I help you today?"
    )
