import sqlite3

# Connect to the database
conn = sqlite3.connect("leetcode.db")
c = conn.cursor()

# Execute a SELECT statement
c.execute("SELECT solution_index FROM file_contents")

# Fetch the results
results = c.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
conn.close()