#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
that start with an uppercase 'N', sorted by states.id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to find states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
    cursor.execute(query)

    # Fetch and print all matching rows
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
