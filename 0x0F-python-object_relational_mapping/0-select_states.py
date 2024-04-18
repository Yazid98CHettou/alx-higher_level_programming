#!/usr/bin/python3
"""return all states """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    data = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         data=argv[3])
    curs = data.cursor()
    curs.execute("""SELECT * FROM states ORDER BY id""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    cusr.close()
    data.close()
