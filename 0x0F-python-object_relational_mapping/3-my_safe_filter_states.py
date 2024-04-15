#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    data = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], data=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name=%s;", (sys.argv[4],))
    [print(states) for states in curs.fetchall()]
