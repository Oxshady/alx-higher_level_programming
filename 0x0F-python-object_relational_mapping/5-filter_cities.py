#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) < 5:
        print("4 arguments needed")
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
            cursor.execute("""select cities.name
                           from cities INNER JOIN states
                           ON
                           cities.state_id = states.id
                           WHERE states.name = %s
                           ORDER BY cities.id ASC;
                           """, (str(argv[4]), ))
            result = cursor.fetchall()
            len = len(result)
            if result:
                for i in range(len):
                    if i == len - 1:
                        print(result[i][0])
                    else:
                        print(result[i][0], end=", ")
            else:
                print()