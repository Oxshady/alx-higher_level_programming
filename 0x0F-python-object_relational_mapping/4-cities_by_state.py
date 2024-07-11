#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) < 4:
        print("3 arguments needed")
        exit(1)

    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]

    with MySQLdb.connect(host='localhost',
                         port=3306,
                         user=db_user,
                         passwd=db_pass,
                         db=db_name) as connector:
        with connector.cursor() as cursor:
            cursor.execute("""select cities.id ,
                           cities.name,
                           states.name from cities INNER JOIN states
                           ON
                           cities.state_id = states.id ORDER BY cities.id ASC;
                           """)
            for row in cursor.fetchall():
                print(row)
