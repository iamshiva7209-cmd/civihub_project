from flask import Flask, render_template, request, redirect, session, url_for
import os
from werkzeug.utils import secure_filename
from db import get_connection
from config import Config
import uuid
app = Flask(__name__)
app.config.from_object(Config)

# ensure upload folders exist
os.makedirs("static/uploads/profile_images", exist_ok=True)
os.makedirs("static/uploads/resumes", exist_ok=True)

# --------------------------
# HOME
# --------------------------

@app.route("/")
def home():
    return render_template("home.html")


# --------------------------
# AUTH
# --------------------------

@app.route("/login", methods=["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
            user = cursor.fetchone()
            conn.close()

            if user:
                from werkzeug.security import check_password_hash
                is_valid = False
                # Check if the password in DB is hashed
                if user["password"].startswith("scrypt:") or user["password"].startswith("pbkdf2:"):
                    is_valid = check_password_hash(user["password"], password)
                else:
                    is_valid = (user["password"] == password)

                if is_valid:
                    session["user_id"] = user["id"]
                    return redirect(url_for("dashboard"))
                else:
                    error = "Invalid password. Please try again."
            else:
                error = "No account found with that email address."
        except Exception as e:
            error = f"Database error: {str(e)}"

    return render_template("auth/login.html", error=error)


@app.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():
    if "pending_user_id" not in session:
        return redirect(url_for("login"))

    error_msg = None
    success_msg = None
    import time

    # Check if this request is from a successful OTP resend
    if request.args.get("resend") == "1":
        success_msg = "A new OTP code has been sent to your phone."

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (session["pending_user_id"],))
    user = cursor.fetchone()
    conn.close()

    if request.method == "POST":
        entered_otp = request.form.get("otp", "").strip()
        otp_code = session.get("otp_code")
        otp_expiry = session.get("otp_expiry", 0)

        if time.time() > otp_expiry:
            error_msg = "OTP has expired. Please log in again."
            session.pop("pending_user_id", None)
            session.pop("otp_code", None)
            session.pop("otp_expiry", None)
        elif entered_otp == otp_code:
            # Login successful
            session["user_id"] = session["pending_user_id"]
            session.pop("pending_user_id", None)
            session.pop("otp_code", None)
            session.pop("otp_expiry", None)
            return redirect(url_for("dashboard"))
        else:
            error_msg = "Invalid OTP code. Please check your number and try again."

    # Mask the phone number for security in UI, e.g. ******7209
    phone = user.get("phone") or ""
    masked_phone = phone
    if len(phone) > 4:
        masked_phone = "*" * (len(phone) - 4) + phone[-4:]

    return render_template("auth/otp.html", masked_phone=masked_phone, error=error_msg, success=success_msg)


@app.route("/resend-otp", methods=["GET"])
def resend_otp():
    if "pending_user_id" not in session:
        return redirect(url_for("login"))

    import random
    import time

    current_user_id = session["pending_user_id"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (current_user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        # Generate new 6-digit OTP
        otp_code = str(random.randint(100000, 999999))
        session["otp_code"] = otp_code
        session["otp_expiry"] = time.time() + 300 # valid for 5 minutes

        # Print to console (Simulating SMS delivery)
        phone_num = user.get("phone") or "No phone number"
        print("\n" + "="*50)
        print(f"[SMS Gateway - RESEND] Sent OTP {otp_code} to phone {phone_num} for user {user['username']}")
        print("="*50 + "\n")

        return redirect(url_for("verify_otp", resend=1))
    
    return redirect(url_for("login"))


# --------------------------
# REGISTER (UPDATED)
# --------------------------



@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        
        from werkzeug.security import generate_password_hash

        username = request.form["username"]
        email = request.form["email"]
        
        # This replaces plain-text entry with a secure cryptographic hash
        password = generate_password_hash(request.form["password"]) 
        
        phone = request.form["phone"]
        location = request.form["location"]
        skills = request.form["skills"]
        qualifications = request.form["qualifications"]
        experience = request.form["experience"]
        portfolio = request.form["portfolio"]

        image = request.files["profile_image"]
        resume = request.files["resume"]


        # --------------------------
        # UNIQUE FILE NAMES
        # --------------------------

        image_name = ""
        resume_name = ""

        if image and image.filename != "":

            ext = image.filename.split(".")[-1]

            image_name = f"profile_{uuid.uuid4().hex}.{ext}"

            image_path = os.path.join(
                "static/uploads/profile_images",
                image_name
            )

            image.save(image_path)


        if resume and resume.filename != "":

            ext = resume.filename.split(".")[-1]

            resume_name = f"resume_{uuid.uuid4().hex}.{ext}"

            resume_path = os.path.join(
                "static/uploads/resumes",
                resume_name
            )

            resume.save(resume_path)


        # --------------------------
        # DB SAVE
        # --------------------------

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO users
        (username,email,password,phone,location,
         skills,qualifications,experience,portfolio,
         profile_image,resume)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            username,
            email,
            password,
            phone,
            location,
            skills,
            qualifications,
            experience,
            portfolio,
            image_name,
            resume_name
        ))

        conn.commit()

        user_id = cursor.lastrowid


        # --------------------------
        # SAVE PROJECTS
        # --------------------------

        project_titles = request.form.getlist("project_title[]")
        project_links = request.form.getlist("project_link[]")
        project_descs = request.form.getlist("project_description[]")

        for title, link, desc in zip(
            project_titles,
            project_links,
            project_descs
        ):

            if title.strip() != "":

                cursor.execute("""
                INSERT INTO projects
                (user_id, project_title, project_link, project_description)
                VALUES(%s,%s,%s,%s)
                """,
                (
                    user_id,
                    title,
                    link,
                    desc
                ))


        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("auth/register.html")


# --------------------------
# DASHBOARD (UPDATED FOR NEW LAYOUT)
# --------------------------

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_connection()
    cursor = conn.cursor()

    # Fetch currently logged-in user details
    cursor.execute(
        "SELECT * FROM users WHERE id=%s",
        (session["user_id"],)
    )

    user = cursor.fetchone()

    # Fetch all user projects to showcase in a feed element
    cursor.execute("""
    SELECT p.*, u.username, u.profile_image 
    FROM projects p 
    JOIN users u ON p.user_id = u.id 
    ORDER BY p.created_at DESC
    """)

    all_projects = cursor.fetchall()

    # Fetch community users to showcase in the sidebar (excluding currently logged-in user)
    cursor.execute(
        "SELECT id, username, profile_image, location FROM users WHERE id != %s LIMIT 5",
        (session["user_id"],)
    )
    community_users = cursor.fetchall()

    # Compute AI grade for badge
    cursor.execute("SELECT * FROM projects WHERE user_id=%s", (session["user_id"],))
    user_projects = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) as cnt FROM projects WHERE user_id=%s", (session["user_id"],))
    post_count = cursor.fetchone()["cnt"]

    cursor.execute("SELECT COUNT(*) as cnt FROM messages WHERE sender_id=%s", (session["user_id"],))
    msg_count = cursor.fetchone()["cnt"]

    conn.close()

    from ai_matcher import grade_user
    grade_info = grade_user(user, user_projects, post_count, msg_count)

    return render_template(
        "dashboard/dashboard.html",
        user=user,
        projects=all_projects,
        community_users=community_users,
        grade=grade_info
    )


# --------------------------
# ADD PROJECT (FROM DASHBOARD)
# --------------------------

@app.route("/add_project", methods=["POST"])
def add_project():

    if "user_id" not in session:
        return redirect(url_for("login"))

    project_title = request.form["project_title"]
    project_link = request.form["project_link"]
    project_description = request.form["project_description"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO projects
    (user_id, project_title, project_link, project_description)
    VALUES(%s,%s,%s,%s)
    """,
    (
        session["user_id"],
        project_title,
        project_link,
        project_description
    ))

    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))


# --------------------------
# JOBS PORTAL
# --------------------------

@app.route("/jobs", methods=["GET"])
def jobs():

    search_query = request.args.get("search", "").strip()
    location_filter = request.args.get("location", "").strip()
    
    conn = get_connection()
    cursor = conn.cursor()

    # Build dynamic query based on filters
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if search_query:
        query += " AND (job_title LIKE %s OR job_description LIKE %s OR company_name LIKE %s)"
        search_pattern = f"%{search_query}%"
        params.extend([search_pattern, search_pattern, search_pattern])

    if location_filter:
        query += " AND location LIKE %s"
        params.append(f"%{location_filter}%")

    query += " ORDER BY posted_date DESC"

    cursor.execute(query, params)
    all_jobs = cursor.fetchall()

    conn.close()

    return render_template(
        "jobs/jobs.html",
        jobs=all_jobs,
        search_query=search_query,
        location_filter=location_filter
    )


# --------------------------
# PROFILE (VIEW + EDIT)
# --------------------------

@app.route("/profile", methods=["GET","POST"])
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_connection()
    cursor = conn.cursor()

    user_id = session["user_id"]

    # UPDATE DETAILS
    if request.method == "POST":

        username = request.form["username"]
        phone = request.form["phone"]
        location = request.form["location"]
        skills = request.form["skills"]
        qualifications = request.form["qualifications"]
        experience = request.form["experience"]
        portfolio = request.form["portfolio"]

        cursor.execute("""
        UPDATE users
        SET username=%s,
            phone=%s,
            location=%s,
            skills=%s,
            qualifications=%s,
            experience=%s,
            portfolio=%s
        WHERE id=%s
        """,
        (
            username,
            phone,
            location,
            skills,
            qualifications,
            experience,
            portfolio,
            user_id
        ))

        conn.commit()


    # GET USER DETAILS
    cursor.execute(
        "SELECT * FROM users WHERE id=%s",
        (user_id,)
    )

    user = cursor.fetchone()


    # GET PROJECTS
    cursor.execute("""
    SELECT * FROM projects
    WHERE user_id=%s
    """,
    (user_id,)
    )

    projects = cursor.fetchall()

    # Compute grade for badge
    cursor.execute("SELECT COUNT(*) as cnt FROM projects WHERE user_id=%s", (user_id,))
    post_count = cursor.fetchone()["cnt"]

    cursor.execute("SELECT COUNT(*) as cnt FROM messages WHERE sender_id=%s", (user_id,))
    msg_count = cursor.fetchone()["cnt"]

    conn.close()

    from ai_matcher import grade_user
    grade_info = grade_user(user, projects, post_count, msg_count)

    return render_template(
        "profile/profile.html",
        user=user,
        projects=projects,
        grade=grade_info
    )

# --------------------------
# CHAT PORTAL
# --------------------------

@app.route("/chat", methods=["GET"])
def chat_index():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_connection()
    cursor = conn.cursor()

    # Find the first user in the DB (excluding current user) to redirect to
    cursor.execute(
        "SELECT id FROM users WHERE id != %s ORDER BY username ASC LIMIT 1",
        (session["user_id"],)
    )
    first_user = cursor.fetchone()
    conn.close()

    if first_user:
        return redirect(url_for("chat", receiver_id=first_user["id"]))
    else:
        return redirect(url_for("chat", receiver_id=0))


@app.route("/chat/<int:receiver_id>", methods=["GET", "POST"])
def chat(receiver_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    current_user_id = session["user_id"]
    conn = get_connection()
    cursor = conn.cursor()

    # If POST request, save message
    if request.method == "POST":
        message_text = request.form.get("message", "").strip()
        if message_text and receiver_id > 0:
            cursor.execute("""
                INSERT INTO messages (sender_id, receiver_id, message)
                VALUES (%s, %s, %s)
            """, (current_user_id, receiver_id, message_text))
            conn.commit()
        conn.close()
        return redirect(url_for("chat", receiver_id=receiver_id))

    # Fetch currently logged-in user details
    cursor.execute("SELECT * FROM users WHERE id = %s", (current_user_id,))
    user = cursor.fetchone()

    # Fetch all other users to display in the sidebar
    cursor.execute(
        "SELECT id, username, profile_image, location FROM users WHERE id != %s ORDER BY username ASC",
        (current_user_id,)
    )
    other_users = cursor.fetchall()

    # Fetch details of the selected receiver
    receiver = None
    messages = []
    if receiver_id > 0:
        cursor.execute("SELECT id, username, profile_image, location FROM users WHERE id = %s", (receiver_id,))
        receiver = cursor.fetchone()

        if receiver:
            # Fetch all messages between current_user and receiver
            cursor.execute("""
                SELECT * FROM messages 
                WHERE (sender_id = %s AND receiver_id = %s)
                   OR (sender_id = %s AND receiver_id = %s)
                ORDER BY created_at ASC
            """, (current_user_id, receiver_id, receiver_id, current_user_id))
            messages = cursor.fetchall()

    conn.close()

    return render_template(
        "chat/chat.html",
        user=user,
        receiver=receiver,
        other_users=other_users,
        messages=messages
    )


# --------------------------
# AI MATCHER + GRADING
# --------------------------

@app.route("/ai")
def ai_page():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_connection()
    cursor = conn.cursor()

    # Fetch user
    cursor.execute("SELECT * FROM users WHERE id=%s", (session["user_id"],))
    user = cursor.fetchone()

    # Fetch user's projects
    cursor.execute("SELECT * FROM projects WHERE user_id=%s", (session["user_id"],))
    projects = cursor.fetchall()

    # Fetch all jobs
    cursor.execute("SELECT * FROM jobs ORDER BY posted_date DESC")
    all_jobs = cursor.fetchall()

    # Count posts (projects shared) and messages for community engagement
    cursor.execute("SELECT COUNT(*) as cnt FROM projects WHERE user_id=%s", (session["user_id"],))
    post_count = cursor.fetchone()["cnt"]

    cursor.execute("SELECT COUNT(*) as cnt FROM messages WHERE sender_id=%s", (session["user_id"],))
    msg_count = cursor.fetchone()["cnt"]

    conn.close()

    # AI computations
    from ai_matcher import score_jobs, grade_user
    job_matches = score_jobs(user, all_jobs)
    grade_info = grade_user(user, projects, post_count, msg_count)

    return render_template(
        "ai/ai.html",
        user=user,
        job_matches=job_matches,
        grade=grade_info,
    )


@app.route("/ai/chat", methods=["POST"])
def ai_chat():
    if "user_id" not in session:
        return redirect(url_for("login"))

    question = request.form.get("question", "").strip()
    if not question:
        return redirect(url_for("ai_page"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id=%s", (session["user_id"],))
    user = cursor.fetchone()

    cursor.execute("SELECT * FROM projects WHERE user_id=%s", (session["user_id"],))
    projects = cursor.fetchall()

    cursor.execute("SELECT * FROM jobs ORDER BY posted_date DESC")
    all_jobs = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) as cnt FROM projects WHERE user_id=%s", (session["user_id"],))
    post_count = cursor.fetchone()["cnt"]

    cursor.execute("SELECT COUNT(*) as cnt FROM messages WHERE sender_id=%s", (session["user_id"],))
    msg_count = cursor.fetchone()["cnt"]

    # --- CONTINUOUS LEARNING: LOGGING ---
    cursor.execute(
        "INSERT INTO ai_conversations (user_id, question) VALUES (%s, %s)",
        (session["user_id"], question)
    )
    conn.commit()

    # --- CONTINUOUS LEARNING: GLOBAL DATA FETCH ---
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    
    cursor.execute("SELECT * FROM projects")
    all_projects = cursor.fetchall()
    
    cursor.execute("SELECT * FROM messages")
    all_messages = cursor.fetchall()
    
    cursor.execute("SELECT question FROM ai_conversations ORDER BY created_at DESC LIMIT 50")
    recent_qs = cursor.fetchall()

    conn.close()

    from ai_matcher import score_jobs, grade_user, get_career_advice
    grade_info = grade_user(user, projects, post_count, msg_count)
    
    # Pass learning context to the AI
    learning_context = {
        "all_users": all_users,
        "all_projects": all_projects,
        "all_messages": all_messages,
        "recent_qs": recent_qs
    }
    answer = get_career_advice(user, all_jobs, grade_info, question, learning_context)

    job_matches = score_jobs(user, all_jobs)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        return {"answer": answer}

    return render_template(
        "ai/ai.html",
        user=user,
        job_matches=job_matches,
        grade=grade_info,
        chat_question=question,
        chat_answer=answer,
    )


# --------------------------
# LOGOUT
# --------------------------

@app.route("/logout")
def logout():

    session.clear()
    return redirect(url_for("home"))


# --------------------------

if __name__ == "__main__":
    app.run(debug=True)