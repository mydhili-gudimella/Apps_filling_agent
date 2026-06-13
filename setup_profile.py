import sqlite3

def create_db():
    conn = sqlite3.connect('formagent.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS profile (
        field TEXT PRIMARY KEY,
        value TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        date TEXT,
        status TEXT
    )''')
    
    conn.commit()
    conn.close()

def fill_profile():
    data = {
        "name": input("Full name: "),
        "email": input("Email: "),
        "phone": input("Phone: "),
        "university": input("University: "),
        "degree": input("Degree: "),
        "cgpa": input("CGPA: "),
        "skills": input("Skills (comma separated): "),
        "projects": input("Projects (brief descriptions): "),
        "internships": input("Internships: "),
        "interests": input("Research interests: "),
        "linkedin": input("LinkedIn URL: "),
        "github": input("GitHub URL: "),
        "about": input("Two sentence bio: ")
    }
    
    conn = sqlite3.connect('formagent.db')
    c = conn.cursor()
    
    for field, value in data.items():
        c.execute("INSERT OR REPLACE INTO profile VALUES (?, ?)", 
                  (field, value))
    
    conn.commit()
    conn.close()
    print("Profile saved.")

create_db()
fill_profile()
