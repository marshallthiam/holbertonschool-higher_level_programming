#!/usr/bin/python3
""" 
Script that takes in arguments and displays all values in the states table 
where name matches the argument (safe from SQL injection).
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2], db=argv[3]
    )

    cur = db.cursor()
    
    # Secure query using parameterized SQL (to avoid SQL injection)
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],))

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
