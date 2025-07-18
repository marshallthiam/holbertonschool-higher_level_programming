#!/usr/bin/python3
"""
3-my_safe_filter_states.py

Lists all values in the states table where name matches the argument.
Uses parameterized query to prevent SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    if len(sys.argv) != 5:
        sys.exit("Usage: ./3-my_safe_filter_states.py <username> <password> <database> <state name>")
    username, password, database, state_name = sys.argv[1:5]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor and execute safe parameterized query
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
