# Job Application Tracker (Python + SQLite)

## Project Description
Job Application Tracker is a Python-based command-line application that helps users manage and track their job applications efficiently.  
The application allows users to add, view, update, and delete job application records using a lightweight SQLite database.

This project demonstrates practical use of Python with SQL and focuses on real-world application development.

---

## Features
- Add new job applications  
- View all job applications  
- Update application status (Applied / Interview / Rejected)  
- Delete job application records  
- Persistent data storage using SQLite  

---

## Technologies Used
- Python  
- SQLite  
- sqlite3 module  

---

## Project Structure
job_application_tracker/
│
├── app.py # Main application logic
├── database.py # Database connection and table creation
└── job_tracker.db # SQLite database (auto-generated)


---

## How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/your-username/job-application-tracker.git


Navigate to the project directory:

cd job-application-tracker


Run the application:

python app.py