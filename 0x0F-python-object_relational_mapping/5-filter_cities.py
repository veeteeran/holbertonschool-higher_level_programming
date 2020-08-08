#!/usr/bin/python3
"""Lists all cities of that state from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT cities.name FROM cities\
            LEFT JOIN states ON cities.state_id = states.id\
            WHERE states.name=%s\
            ORDER by cities.id ASC"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    for row in range(len(rows)):
        print(rows[row][0], end='')
        if row < len(rows) - 1:
            print(', ', end='')
    print()

    cur.close()
    db.close()
