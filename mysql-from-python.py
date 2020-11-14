import os
import pymysql

# Get username from workspace, who knows?

username = os.getenv('GG_USER')

# Connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()