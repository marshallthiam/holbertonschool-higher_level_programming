#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Collect arguments
    username, password, dbname, state_name = sys.argv[1:5]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Create cursor and execute parameterized query
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Cleanup
    cursor.close()
    db.close()
