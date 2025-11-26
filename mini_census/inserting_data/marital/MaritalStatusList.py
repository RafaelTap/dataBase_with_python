import mysql.connector

try:
    connection = mysql.connector.connect(database='census_db',
                                         username='root',
                                         password='rafael@dev',
                                         host='localhost',
                                         port='3306')

    cursor = connection.cursor()

    command = """SELECT marital_status FROM marital_status"""

    cursor.execute(command)

    MaritalStatus_list = cursor.fetchall()

    for marital_list in MaritalStatus_list:
        print('marital status: ', marital_list)

except mysql.connector.DatabaseError as error:
    print(error)
finally:
    cursor.close()

