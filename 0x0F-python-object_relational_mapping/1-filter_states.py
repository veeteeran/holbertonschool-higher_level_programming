#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
