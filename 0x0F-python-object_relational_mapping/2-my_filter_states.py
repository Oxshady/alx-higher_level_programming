#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Results must be sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv
if len(argv) < 5:
    print("4 argument required")
    exit()
db_user = argv[1]
db_pass = argv[2]
db_name = argv[3]
state = argv[4]
s = "SELECT * from states WHERE name = %s ORDER BY id ASC"
try:
    connection = MySQLdb.connect(user=db_user, passwd=db_pass, db=db_name)
    with connection:
        cursor = connection.cursor()
        with cursor:
            cursor.execute(s, (state,))
            print(cursor.fetchone())
except MySQLdb.Error as err:
    print(f"mysqldb error the error is:{err}")
