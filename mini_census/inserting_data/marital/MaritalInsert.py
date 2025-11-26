import mysql.connector

try:
    connection = mysql.connector.connect(database='census_db',
                                         username='root',
                                         password='rafael@dev',
                                         host='localhost',
                                         port='3306')

    cursor = connection.cursor()

    command = """ INSERT INTO marital_status (marital_status) VALUES (%(marital_status)s)"""

    data = [{'marital_status':'single'},
            {'marital_status':'married'},
            {'marital_status':'divorced'},
            {'marital_status':'widow'}]

    cursor.executemany(command, data)
    connection.commit()

except mysql.connector.DatabaseError as error:
    print(error)
finally:
    cursor.close()
    connection.close()