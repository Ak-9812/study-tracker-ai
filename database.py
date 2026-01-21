import sqlite3

conn = sqlite3.connect("study.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS study_sessions (
    date TEXT,
    subject TEXT,
    topics TEXT,
    time INTEGER,
    done BOOLEAN
)
""")
conn.commit()

def add_session(date, subject, topics, time, done):
    cursor.execute(
        "INSERT INTO study_sessions VALUES (?, ?, ?, ?, ?)",
        (str(date), subject, topics, time, done)
    )
    conn.commit()

def get_all_sessions():
    cursor.execute("SELECT * FROM study_sessions")
    return cursor.fetchall()
