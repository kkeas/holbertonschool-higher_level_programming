#!/usr/bin/python3
"""comment"""
import MySQLdb
import sys

if __name__ == '__main__':
    con = MySQLdb.connect(usr=sys.argv[1], passwrd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states")
    [print(state) for state in cursor.fetchall()]
