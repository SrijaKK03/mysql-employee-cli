import mysql.connector

try:
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",  # replace with your actual password
        database="employee_db"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    print("\n📋 Employee Records:\n")
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
