import sqlite3
from fastapi import FastAPI

app = FastAPI()

# Create a function to retrieve the file contents based on the solution index
def get_file_contents(index: str) -> str:
    conn = sqlite3.connect('leetcode.db')
    cursor = conn.cursor()

    # Execute the SELECT query to retrieve the file contents for the given index
    cursor.execute("SELECT contents FROM file_contents WHERE solution_index=?", (index,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Check if a file contents were found for the given index
    if result is None:
        return f"No file contents found for index {index}"

    # Return the file contents as a string
    return result[0]

# Define a route to retrieve the file contents based on the solution index
@app.get("/solution/{index}")
async def get_solution(index: str):
    # Retrieve the file contents for the given index
    contents = get_file_contents(index)

    # Return the file contents as a JSON response
    # print(contents)
    return {"contents": contents}
