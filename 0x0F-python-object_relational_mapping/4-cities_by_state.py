#!/usr/bin/python3
"""return cities and states """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    curso = db.cursor()
    curso.execute("""SELECT c.id, c.name, s.name FROM cities c
                JOIN states s ON c.state_id = s.id""")
    rows = curso.fetchall()
    for row in rows:
        print(row)
    curso.close()
    db.close()
