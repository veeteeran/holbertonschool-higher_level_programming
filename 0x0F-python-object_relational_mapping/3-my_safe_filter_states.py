#!/usr/bin/python3
"""Takes in argument, displays all values in states table"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name=%s\
            ORDER by states.id ASC"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
