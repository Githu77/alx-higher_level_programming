#!/usr/bin/python3


import MySQLdb
from sys import argv

'''states with N in starting name'''
if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%'ORDER BY id ASC")
    db = cursor.fetchall()
    for x in db:
        print(x)