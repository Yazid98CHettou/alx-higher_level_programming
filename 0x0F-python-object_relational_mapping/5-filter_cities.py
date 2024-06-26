#!/usr/bin/python3
"""return cities and states"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    crs = db.cursor()
    crs.execute("""SELECT c.name FROM cities c
                LEFT JOIN states s ON c.state_id = s.id
                WHERE s.name LIKE BINARY %s
                ORDER BY c.id ASC""", (argv[4],))
    rows = crs.fetchall()
    cont = 0
    lista = []
    for row in rows:
        lista.append(row[0])
    print(", ".join(lista))
    crs.close()
    db.close()
