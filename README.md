# 🐍 MySQL Employee CLI Tool

This is a simple Python command-line project to manage employee records using MySQL. It allows you to connect to a MySQL database and perform basic operations such as viewing, adding, deleting, and updating employee records. It’s perfect for beginners learning how Python and MySQL work together.


## 📁 Project Overview

This project includes the following files:

| File Name                  | Purpose                                                   |
| -------------------------- | --------------------------------------------------------- |
| `test_mysql_connection.py` | To test whether Python is connected to MySQL successfully |
| `employee_cli.py`          | CLI-based script to interact with the database            |

---

## 🧱 Requirements

Before you run the code, make sure you have:

* Python installed (version 3.6+ recommended)
* MySQL installed and running
* MySQL Connector installed for Python
  Install it using pip:

  ```bash
  pip install mysql-connector-python
  ```

---

## 💄 MySQL Database Setup

Follow these steps to create and populate your database:

### Step 1: Open the MySQL terminal

```bash
mysql -u root -p
```

Enter your password when prompted.

### Step 2: Create the database and table

```sql
CREATE DATABASE employee_db;
USE employee_db;

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);

INSERT INTO employees (name, age, department) VALUES
('Alice', 30, 'Engineering'),
('Bob', 25, 'HR'),
('Charlie', 28, 'Marketing');
```

---

## 🧪 Test the MySQL Connection

Run this Python file to check if Python can connect to MySQL:

```bash
python test_mysql_connection.py
```

✅ **Expected Output:**

```
Connected to MySQL database successfully!
```

---

## 💻 Use the CLI Tool

This is the main file that gives you a menu-based system to interact with the employee database:

```bash
python employee_cli.py
```

💡 **Example Menu:**

```
==== Employee Management ====
1. Add Employee
2. View Employees
3. Update Employee
4. Delete Employee
5. Exit
Enter choice: 1
```

---

## 💡 Summary 

1. Installed Python & MySQL
2. Created the database `employee_db` and `employees` table
3. Added some sample employee data
4. Created Python scripts to:

   * Connect to MySQL
   * Show menu to Add, View, Update, Delete employees
5. Tested the connection using `test_mysql_connection.py`





