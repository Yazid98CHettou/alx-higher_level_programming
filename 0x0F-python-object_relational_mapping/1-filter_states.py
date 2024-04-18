#!/usr/bin/python3
"""return filter states """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    datab = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         datab=argv[3])
    curs = datab.cursor()
    curs.execute("""SELECT * FROM states WHERE
                name LIKE BINARY "N%" ORDER BY id""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    datab.close()
