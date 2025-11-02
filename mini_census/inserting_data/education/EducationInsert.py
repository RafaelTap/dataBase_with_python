import mysql.connector

try:
    connection = mysql.connector.connect(database= "census_db",
                                         username= "root",
                                         password= "rafael@dev",
                                         host= "localhost",
                                         port= "3306")
    cursor = connection.cursor()

    command = """ INSERT INTO education (education) 
                  VALUES ('post-graduated(MBA)')"""

    cursor.execute(command)
    connection.commit()

except mysql.connector.DatabaseError as error:
    print(error)
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()
