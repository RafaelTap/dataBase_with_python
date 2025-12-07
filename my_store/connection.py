import psycopg2 as connector

connection = connector.connect(database='store_db',
                               user='postgres',
                               password='rafael@dev',
                              host='localhost',
                              port='5432')

cursor = connection.cursor()

