#!/usr/bin/python3
"""return filter states """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    curso = db.cursor()
    curso.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY id""".format(argv[4]))
    rows = curso.fetchall()
    for row in rows:
        print(row)
    curso.close()
    db.close()
