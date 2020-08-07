#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            LEFT JOIN states ON cities.state_id = states.id\
            ORDER by cities.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
