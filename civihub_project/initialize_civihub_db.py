import pymysql
from werkzeug.security import generate_password_hash

def init_db():
    # Connect to MySQL server
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = conn.cursor()
    
    # Create Database
    cursor.execute("CREATE DATABASE IF NOT EXISTS civihub CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    cursor.execute("USE civihub;")
    
    # Create Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(150) DEFAULT NULL,
        email VARCHAR(150) UNIQUE,
        password VARCHAR(255) DEFAULT NULL,
        phone VARCHAR(20) DEFAULT NULL,
        location VARCHAR(150) DEFAULT NULL,
        experience VARCHAR(50) DEFAULT NULL,
        skills TEXT,
        qualifications TEXT,
        portfolio TEXT,
        profile_image VARCHAR(255) DEFAULT NULL,
        resume VARCHAR(255) DEFAULT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """)
    
    # Create Projects Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT DEFAULT NULL,
        project_title VARCHAR(200) DEFAULT NULL,
        project_link VARCHAR(255) DEFAULT NULL,
        project_description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """)
    
    # Create Messages Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        sender_id INT NOT NULL,
        receiver_id INT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (receiver_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """)
    
    # Create Jobs Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        job_title VARCHAR(200) NOT NULL,
        company_name VARCHAR(150) NOT NULL,
        location VARCHAR(150) DEFAULT NULL,
        job_description TEXT,
        skills_required TEXT,
        salary_range VARCHAR(100) DEFAULT NULL,
        posted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """)
    
    # Create AI Conversations Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ai_conversations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        question TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """)
    
    # Seed Jobs
    cursor.execute("SELECT COUNT(*) as cnt FROM jobs")
    if cursor.fetchone()[0] == 0:
        jobs_data = [
            ("Senior Structural Engineer", "BuildCorp Infrastructure", "Mumbai, India", 
             "We are looking for a Senior Structural Engineer to design and analyze structures, manage projects, and oversee site development.", 
             "autocad, revit, staad pro, structural analysis, concrete, steel", "$15,000 - $22,000 / Year"),
            ("BIM Modeler & Coordinator", "ArchTech Solutions", "Bangalore, India", 
             "Join our BIM modeling team. Responsibilities include building structural layouts, coordinating with design teams, and managing CAD documents.", 
             "revit, bim, autocad, civil 3d, navisworks", "$10,000 - $14,000 / Year"),
            ("Geotechnical Site Engineer", "GeoFoundation Ltd", "Delhi, India", 
             "Responsible for soil investigations, foundation recommendations, and on-site testing for tunnel and highway projects.", 
             "geotechnical, soil mechanics, foundation, concrete, site supervision", "$9,000 - $12,000 / Year"),
            ("Project Planner & Scheduler", "Apex Construction Group", "Mumbai, India", 
             "Looking for an experienced Planner to develop construction schedules, monitor budgets, and work with Primavera P6 / MS Project.", 
             "primavera, ms project, planning, scheduling, construction management, project management", "$12,000 - $18,000 / Year"),
            ("Junior Civil Inspector", "Metro Rail Corporation", "Pune, India", 
             "Entry-level position for site inspections, quality checks, land surveying, and general project coordination.", 
             "surveying, autocad, estimation, quality control, site supervision", "$6,000 - $8,000 / Year")
        ]
        cursor.executemany("""
        INSERT INTO jobs (job_title, company_name, location, job_description, skills_required, salary_range)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, jobs_data)
        print("Seeded sample jobs.")
        
    # Seed Community Users
    cursor.execute("SELECT COUNT(*) as cnt FROM users")
    if cursor.fetchone()[0] == 0:
        hashed_password = generate_password_hash("password")
        users_data = [
            ("Arjun Mehta", "arjun@civihub.com", hashed_password, "+919876543210", "Mumbai, India", "8", 
             "autocad, structural analysis, concrete, steel, staad pro", "B.Tech in Civil Engineering", 
             "https://github.com/arjunmehta", "profile_arjun.png", ""),
            ("Priya Sharma", "priya@civihub.com", hashed_password, "+919876543211", "Bangalore, India", "4", 
             "revit, bim, autocad, civil 3d, navisworks", "M.Tech in Structural Engineering", 
             "https://behance.net/priyasharma", "profile_priya.png", ""),
            ("Rahul Verma", "rahul@civihub.com", hashed_password, "+919876543212", "Delhi, India", "10", 
             "primavera, planning, construction management, safety, cost estimation", "MBA in Construction Management", 
             "https://linkedin.com/in/rahulverma", "profile_rahul.png", ""),
            ("Neha Goel", "neha@civihub.com", hashed_password, "+919876543213", "Pune, India", "2", 
             "surveying, total station, autocad, estimation, excel", "B.Tech in Civil Engineering", 
             "", "profile_neha.png", "")
        ]
        cursor.executemany("""
        INSERT INTO users (username, email, password, phone, location, experience, skills, qualifications, portfolio, profile_image, resume)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, users_data)
        print("Seeded community users.")
        
    conn.commit()
    conn.close()
    print("Database initialized and seeded successfully!")

if __name__ == "__main__":
    init_db()
