import mysql.connector

try:
    connection = mysql.connector.connect(database='census_db',
                                         username='root',
                                         password='rafael@dev',
                                         host='localhost',
                                         port='3306')

    cursor = connection.cursor()

    command = """ SELECT * FROM address"""

    cursor.execute(command)

    full_list = cursor.fetchall()

    for address_list in full_list:
        print("address: ", address_list)

except mysql.connector.DatabaseError as error:
    print(error)
finally:
    cursor.close()