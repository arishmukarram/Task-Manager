import mysql.connector

# MySQL database connection settings
config = {
    'user': 'node41',
    'password': "root",
    'host': "root",
    'database': "todolist",
}

# Establish a connection to the database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Create the tasks table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT,
    task VARCHAR(255),
    priority VARCHAR(10),
    due_date DATE,
    category VARCHAR(50),
    recurrence VARCHAR(10),
    completed BOOLEAN DEFAULT FALSE,
    notes TEXT,
    archived BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id)
);
""")

def add_task():
    task = input("Enter task: ")
    priority = input("Enter priority (High, Medium, Low): ")
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ") or None
    category = input("Enter category (e.g., Work, Personal): ")
    recurrence = input("Enter recurrence (daily, weekly, monthly) or leave blank: ") or None
    notes = input("Enter additional notes or leave blank: ") or None
    
    query = "INSERT INTO tasks (task, priority, due_date, category, recurrence, notes) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (task, priority, due_date, category, recurrence, notes))
    cnx.commit()
    print("Task added successfully!")

def view_tasks():
    query = "SELECT * FROM tasks WHERE archived = FALSE"
    cursor.execute(query)
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"{task[0]} - {task[1]} - Priority: {task[2]} - Due: {task[3]} - Category: {task[4]} - Completed: {task[6]}")

def delete_task():
    query = "SELECT * FROM tasks WHERE archived = FALSE"
    cursor.execute(query)
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"{task[0]} - {task[1]}")
            
        task_id = int(input("Enter task number to delete: "))
        query = "DELETE FROM tasks WHERE id = %s"
        cursor.execute(query, (task_id,))
        cnx.commit()
        print("Task deleted successfully!")

def modify_task():
    query = "SELECT * FROM tasks WHERE archived = FALSE"
    cursor.execute(query)
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"{task[0]} - {task[1]}")
            
        task_id = int(input("Enter task number to modify: "))
        new_task = input("Enter the new task description: ")
        new_priority = input("Enter the new priority (High, Medium, Low): ")
        new_due_date = input("Enter the new due date (YYYY-MM-DD) or leave blank: ") or None
        new_category = input("Enter the new category or leave blank: ") or None
        new_recurrence = input("Enter the new recurrence (daily, weekly, monthly) or leave blank: ") or None
        new_notes = input("Enter additional notes or leave blank: ") or None
        
        query = """
        UPDATE tasks
        SET task = %s, priority = %s, due_date = %s, category = %s, recurrence = %s, notes = %s
        WHERE id = %s
        """
        cursor.execute(query, (new_task, new_priority, new_due_date, new_category, new_recurrence, new_notes, task_id))
        cnx.commit()
        print("Task modified successfully!")

def complete_task():
    query = "SELECT * FROM tasks WHERE archived = FALSE"
    cursor.execute(query)
    tasks = cursor.fetchall()
    
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"{task[0]} - {task[1]}")
            
        task_id = int(input("Enter task number to mark as completed: "))
        query = "UPDATE tasks SET completed = TRUE WHERE id = %s"
        cursor.execute(query, (task_id,))
        cnx.commit()
        print("Task marked as completed.")

def archive_completed_tasks():
    query = "UPDATE tasks SET archived = TRUE WHERE completed = TRUE"
    cursor.execute(query)
    cnx.commit()
    print("Completed tasks archived.")

def view_archived_tasks():
    query = "SELECT * FROM tasks WHERE archived = TRUE"
    cursor.execute(query)
    tasks = cursor.fetchall()
    
    if not tasks:
        print("No archived tasks available.")
    else:
        for task in tasks:
            print(f"{task[0]} - {task[1]} - Archived")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Modify Task")
        print("5. Complete Task")
        print("6. Archive Completed Tasks")
        print("7. View Archived Tasks")
        print("8. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            modify_task()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            archive_completed_tasks()
        elif choice == "7":
            view_archived_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()