import mysql.connector

try:
    connection = mysql.connector.connect(database= "census_db",
                                         username= "root",
                                         password= "rafael@dev",
                                         host= "localhost",
                                         port= "3306")
    cursor = connection.cursor()


    data = [{'education_level':'daycare'},
            {'education_level':'preschool'},
            {'education_level':'elementary school'},
            {'education_level':'middle school'},
            {'education_level':'High school'},
            {'education_level':'technical course'},
            {'education_level':'Post-Secondary Technical Course'},
            {'education_level':'Bachelor’s Degree'},
            {'education_level':'teaching Degree'},
            {'education_level':'Postgraduate Certificate'},
            {'education_level':'Master’s Degree'},
            {'education_level':'Professional Master’s Degree'},
            {'education_level':'PhD'},
            {'education_level':'Postdoc'}
            ]

    command = """ INSERT INTO education (education_level) 
                  VALUES (%(education_level)s)"""

    cursor.executemany(command, data)
    connection.commit()

except mysql.connector.DatabaseError as error:
    print(error)
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()
