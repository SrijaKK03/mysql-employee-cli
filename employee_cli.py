import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",  # 🔁 Replace with your MySQL password
    database="employee_db"
)

cursor = conn.cursor()

def add_employee():
    name = input("Enter name: ")
    age = input("Enter age: ")
    department = input("Enter department: ")
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", (name, age, department))
    conn.commit()
    print("✅ Employee added successfully.\n")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)
    print()

def search_employee():
    emp_id = input("Enter employee ID to search: ")
    cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
    result = cursor.fetchone()
    if result:
        print(result)
    else:
        print("❌ Employee not found.\n")

def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    cursor.execute("DELETE FROM employees WHERE id = %s", (emp_id,))
    conn.commit()
    print("🗑️ Employee deleted (if existed).\n")

def main():
    while True:
        print("\n--- Employee Records CLI ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Delete Employee by ID")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            break
        else:
            print("⚠️ Invalid choice.\n")

if __name__ == "__main__":
    main()
