#!/usr/bin/python3
"""Takes in argument, displays all values in states table"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name='{}'\
            ORDER by states.id ASC".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
