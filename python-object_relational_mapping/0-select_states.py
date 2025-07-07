#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute query to select all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all rows
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
