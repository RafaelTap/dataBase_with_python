import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(database='census_db',
                                         user='root',
                                         password='rafael@dev',
                                         host='localhost',
                                         port='3306')
    cursor = connection.cursor()

    command = """INSERT INTO income (monthly_income) VALUE (%s)"""

    data = [(2000,),
            (3000,),
            (4000,),
            (5000,),
            (6000,),
            (7000,),
            (8000,),
            (9000,),
            (10000,),
            (15000,)]

    cursor.executemany(command, data)
    connection.commit()


except Error as err:
    print(err)
finally:
    cursor.close()
    connection.close()
