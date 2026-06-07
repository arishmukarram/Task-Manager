# Command-Line TaskManager 

A lightweight, persistent task management system built with Python and MySQL. This application allows users to perform full CRUD (Create, Read, Update, Delete) operations on their daily tasks via a streamlined command-line interface.

## Features
* Task Management: Add, view, modify, and delete tasks dynamically.
* Data Persistence: All inputs are instantly written to a local MySQL database, ensuring zero data loss between sessions.
* Status Tracking: Mark specific tasks as completed to track daily progress.
* Archive System: Push completed tasks to a dedicated archive table to keep the active workflow interface clean and readable.

## Tech Stack
* Language: Python 3.x
* Database: MySQL
* Dependencies:`mysql-connector-python`

## Setup Instructions 
### 1.Clone repository:
   `git clone [https://github.com/arsihmukarram/Task-Manager.git](https://github.com/arsihmukarram/Task-Manager.git)
   cd Task-Manager`
### 2.Configure The Database Connection:
   Open the todo_list.py file and update the config dictionary with your local MySQL credentials
   `config = {
    'user': 'YOUR_MYSQL_USERNAME',
    'password': "YOUR_MYSQL_PASSWORD",
    'host': "localhost", 
    'database': "todolist"}`
### 3.Run Application:
   Execute the script from your terminal. The application will automatically create the necessary tasks table within your MySQL database if it does not already exist.
    `python todo_list.py`
   
## Prerequisites
To run this application locally, you must have Python and MySQL installed on your machine. You will also need the official MySQL connector for Python:
```bash
pip install mysql-connector-python 
```

## Live Demonstration
### 1.Database Architecture
   The backend is powered by a relational MySQL structure to ensure data persistence.
   ```
    mysql> DESC tasks;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| task       | varchar(255) | NO   |     | NULL    |                |
| priority   | varchar(10)  | YES  |     | NULL    |                |
| due_date   | date         | YES  |     | NULL    |                |
| category   | varchar(50)  | YES  |     | NULL    |                |
| recurrence | varchar(20)  | YES  |     | NULL    |                |
| notes      | text         | YES  |     | NULL    |                |
| completed  | boolean      | YES  |     | 0       |                |
+------------+--------------+------+-----+---------+----------------+
```
### 2.Application Interface
The terminal provides a clean, continuous loop for all CRUD operations.

```text
--- To-Do List ---
1. Add Task
2. View Tasks
3. Delete Task
4. Modify Task
5. Complete Task
6. Archive Completed Tasks
7. View Archived Tasks
8. Exit

Choose an option: 1
Enter task: Finish project report
Enter priority (High, Medium, Low): High
Enter due date (YYYY-MM-DD) or leave blank: 2024-10-01
Enter category (e.g., Work, Personal): Work
Enter recurrence (daily, weekly, monthly) or leave blank: weekly
Enter additional notes or leave blank: Remember to include financial analysis
Task added successfully!
```
### 3. Backend Data Verification
State changes made in the terminal immediately update the database records.
```
mysql> SELECT * FROM tasks;
+----+-----------------------+----------+------------+----------+------------+-----------+
| id | task                  | priority | due_date   | category | recurrence | completed |
+----+-----------------------+----------+------------+----------+------------+-----------+
| 1  | Finish project report | High     | 2024-10-01 | Work     | weekly     | 0         |
+----+-----------------------+----------+------------+----------+------------+-----------+
```
