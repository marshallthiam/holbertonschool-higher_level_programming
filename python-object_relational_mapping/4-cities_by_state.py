#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

def list_cities():
    # Get MySQL credentials and database name from command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute the query
    cur = db.cursor()

    # Execute a single query to fetch city and state data
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Fetch and print all results
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()

if __name__ == "__main__":
    list_cities()
