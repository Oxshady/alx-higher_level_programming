#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Results must be sorted in ascending order by states.id
"""
import MySQLdb
try:
    connection = MySQLdb.connect(user="shadi", passwd="1", db="hbtn_0e_0_usa")
    with connection:
        cursor = connection.cursor()
        with cursor:
            cursor.execute("SELECT * from states ORDER BY id ASC")
            for row in cursor.fetchall():
                print(row)
except MySQLdb.Error as err:
    print(f"mysqldb error the error is:{err}")
