#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    data = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], data=sys.argv[3])

    curs = data.cursor()
    curs.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in curs.fetchall()]
