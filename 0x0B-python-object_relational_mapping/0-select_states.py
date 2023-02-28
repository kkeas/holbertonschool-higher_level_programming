#!/usr/bin/python3
"""comment"""

import SQLdb
import sys

if __name__ == '__main__':
    connection = SQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")
    [print(state) for state in cursor.fetchall()]
