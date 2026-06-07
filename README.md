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
* Clone repository:
   `git clone [https://github.com/arsihmukarram/TaskManager.git](https://github.com/arsihmukarram/TaskManager.git)
   cd TaskManager`
* Configure The Database Connection:
   Open the todo_list.py file and update the config dictionary with your local MySQL credentials
   `config = {
    'user': 'YOUR_MYSQL_USERNAME',
    'password': "YOUR_MYSQL_PASSWORD",
    'host': "localhost", 
    'database': "todolist"}`
*Run Application:
   Execute the script from your terminal. The application will automatically create the necessary tasks table within your MySQL database if it does not already exist.
    `python todo_list.py`
   
## Prerequisites
To run this application locally, you must have Python and MySQL installed on your machine. You will also need the official MySQL connector for Python:
```bash
pip install mysql-connector-python 
