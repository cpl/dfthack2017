#!/usr/bin/python
"""DOCSTRING."""

import MySQLdb
import config

# connect
db = MySQLdb.connect(host=config.HOSTNAME, user=config.USERNAME,
                     passwd=config.PASSWORD, db=config.DATABASE)

cursor = db.cursor()

# execute SQL select statement
cursor.execute("SELECT * FROM ROUTES")

# commit your changes
db.commit()

# get the number of rows in the resultset
numrows = int(cursor.rowcount)

# get and display one row at a time.
for x in range(0, numrows):
    row = cursor.fetchone()
    print row
