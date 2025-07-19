#!/usr/bin/python3
"""List all cities of a given state (safe from SQL injection)"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name, state_name = sys.argv[1:5]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cur = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cur.execute(query, (state_name,))

    # Fetch all matching rows
    cities = cur.fetchall()

    # Print city names as a comma-separated string
    print(", ".join([city[0] for city in cities]))

    # Clean up
    cur.close()
    db.close()
