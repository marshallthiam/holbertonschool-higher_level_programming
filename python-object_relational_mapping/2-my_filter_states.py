#!/usr/bin/python3
""" Script that lists all values in the states table
    where name matches the argument (safe from SQL injections).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Create a cursor
    cur = db.cursor()

    # Create and execute query using format (not safe for user input in general)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch and print results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Clean up
    cur.close()
    db.close()
