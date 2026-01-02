from database import connect_db

def add_job():
    company = input("Company Name : ")
    role = input("Job Role : ")
    date = input("Date applied (yyyy-mm-dd): ")
    status = input("Status (Applied/Interview/Rejected) : ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO jobs (company, role, date_applied, status) VALUES (?, ?, ?, ?)",(company,role,date,status))

    conn.commit()
    conn.close()

    print("Job Added successfully✅")

def view_jobs():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()

    print("\n Job Applications:")

    for row in rows:
        print(row)
    
    cursor.close()

def update_status():
    view_jobs()
    job_id = input("Enter Job Id : ")
    new_status = input("New Status : ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("UPDATE jobs SET status = ? WHERE id = ?", (new_status, job_id))
    conn.commit()
    conn.close()
    print("\n Job status updated successfully✅")

def delete_job():
    job_id = input("Enter Job ID to delete: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()
    print("Job deleted!")
 
def menu():
    while True:
        print("\n--- Job Application Tracker ---")
        print("1. Add Job")
        print("2. View Jobs")
        print("3. Update Job Status")
        print("4. Delete Job")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_job()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")

menu()
