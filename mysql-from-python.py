import os
import datetime
import pymysql

# Get username from workspace, who knows?

username = os.getenv('OG_USER')

# Connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # the above will display a warning, not an error, if the table already exists
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()