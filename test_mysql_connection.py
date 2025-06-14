import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_db"
)

cursor = conn.cursor()

# Fetch all employees
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
