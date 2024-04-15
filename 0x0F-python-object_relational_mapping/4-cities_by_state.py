#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    data = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], data=sys.argv[3])
    curs = data.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id")
    [print(cities) for cities in curs.fetchall()]
