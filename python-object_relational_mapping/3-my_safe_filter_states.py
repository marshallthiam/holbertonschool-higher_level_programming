#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line args
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to DB
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=db_name)

    cur = db.cursor()

    # Execute a safe parameterized query
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
