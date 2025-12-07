import mysql.connector

try:
    connection = mysql.connector.connect(database='census_db',
                                         username='root',
                                         password='rafael@dev',
                                         host='localhost',
                                         port='3306')

    cursor = connection.cursor()

    command = """ select education_level from education """

    cursor.execute(command)

    educationLevel_list = cursor.fetchall()

    for level in educationLevel_list:
        print("education level: ", level)

except mysql.connector.DatabaseError as error:
    print(error)
except Exception as error:
    print(error)
finally:
    cursor.close()
