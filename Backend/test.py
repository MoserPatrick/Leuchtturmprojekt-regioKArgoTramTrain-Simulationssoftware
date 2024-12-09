import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password='Password',
                              host='localhost',
                              database='kvv')
cursor = cnx.cursor()

query = 'SELECT * FROM s3_h'
cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
cnx.close()