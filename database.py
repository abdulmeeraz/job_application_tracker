import sqlite3

def connect_db():
    return sqlite3.connect("job_tracker.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        role TEXT NOT NULL,
        date_applied TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()

create_table()
