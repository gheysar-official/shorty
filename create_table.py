# Script to build mysql table
import psycopg2

import config
from sql_table import URLs_table,log_table

'''
Create_table.py looks for MySQL Config in config.py 
Creates a connection to the database using the supplied config

Creates a TABLE named WEB_URL with the specified rows.
Needs to RUN once when setting up the application on local or
web server.

You need to have a database already defined ( SHORTY for e.g is 
already present .).
'''
host = config.host
user = config.user
passwrd = config.passwrd
db = config.db


conn = psycopg2.connect(host=host, user=user, password=passwrd, database=db)

cursor = conn.cursor()

cursor.execute(URLs_table)
cursor.execute(log_table)

conn.commit()
conn.close()
