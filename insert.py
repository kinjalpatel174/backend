#Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.
import sqlite3

# 1. Connect to SQLite3 database (or create it if it doesn't exist)
conn = sqlite3.connect("school.db")

# 2. Create a cursor object to execute SQL queries
cursor = conn.cursor()

# 3. Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# 4. Insert data into the table
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Kinjal", 20))
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("uma", 22))
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("kamini", 19))

# Commit the changes
conn.commit()

# 5. Fetch data from the table
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

# Display the fetched data
print("Student Records:")
for row in rows:
    print(row)

# 6. Close the database connection
conn.close()
