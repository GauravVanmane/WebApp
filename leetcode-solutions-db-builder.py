import os
import sqlite3
import subprocess
# Clone the repository
repo_url = "https://github.com/AshwinRachha/LeetCode-Solutions"
repo_name = os.path.basename(repo_url.rstrip("/"))
if not os.path.isdir(repo_name):
    subprocess.run(["git", "clone", repo_url])
# Connect to the SQLite database
db_filename = "leetcode.db"

if os.path.isfile(db_filename):
    os.remove(db_filename)

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
# Create the table to store filename and contents
cursor.execute("""
    CREATE TABLE IF NOT EXISTS file_contents (
        solution_index TEXT PRIMARY KEY,
        contents TEXT
    )
""")
# Walk through each subdirectory
for root, dirs, files in os.walk(repo_name):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                contents = f.read()
            # Insert filename and contents into the database
            solution_index = file.split("-")[0]
            print(solution_index)
            cursor.execute("""
                INSERT INTO file_contents (solution_index, contents) VALUES (?, ?)
            """, (solution_index, contents))
# Commit changes and close the database connection
conn.commit()
conn.close()
print("Indexing complete!")