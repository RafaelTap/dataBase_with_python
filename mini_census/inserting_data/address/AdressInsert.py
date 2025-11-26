import mysql.connector

try:
    connection = mysql.connector.connect(database='census_db',
                                         username='root',
                                         password='rafael@dev',
                                         host='localhost',
                                         port='3306')

    cursor = connection.cursor()

    #command = """INSERT INTO address (street, number, complement, neighborhood, city, zipcode)
    #             VALUES (%(street)s, %(number)s, %(complement)s, %(neighborhood)s, %(city)s, %(zipcode)s)""" (used with
    # dictionary.

    command = """INSERT INTO address (street, number, complement, neighborhood, city, zipcode) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""

    data = [('Maple Street', 102, 'Apt 2A', 'Downtown', 'Springfield', '90210'),
            ('Oak Avenue', 55, None, 'Downtown', 'Springfield', '90211'),
            ('Pine Road', 331, None, 'Downtown', 'Springfield', '90212'),
            ('Cedar Lane', 48, 'Suite 10', 'Downtown', 'Springfield', '90213'),
            ('Birch Boulevard', 20, None, 'Downtown', 'Springfield', '90214'),
            ('Willow Street', 87, 'House B', 'Old Town', 'Riverside', '90301'),
            ('Elm Avenue', 12, None, 'Old Town', 'Riverside', '90302'),
            ('Chestnut Road', 144, None, 'Old Town', 'Riverside', '90303'),
            ('Walnut Street', 72, 'Apt 4', 'Old Town', 'Riverside', '90304'),
            ('Ash Boulevard', 250, None, 'Old Town', 'Riverside', '90305'),
            ('River Street', 93, None, 'Greenfield', 'Brookdale', '90401'),
            ('Hill Avenue', 78, 'Floor 3', 'Greenfield', 'Brookdale', '90402'),
            ('Forest Drive', 125, None, 'Greenfield', 'Brookdale', '90403'),
            ('Park Road', 212, 'Suite 5B', 'Greenfield', 'Brookdale', '90404'),
            ('Sunset Boulevard', 301, None, 'Greenfield', 'Brookdale', '90405'),
            ('Lakeside Street', 16, None, 'West End', 'Fairview', '90501'),
            ('Highland Avenue', 45, 'Unit 2', 'West End', 'Fairview', '90502'),
            ('Main Street', 118, None, 'West End', 'Fairview', '90503'),
            ('Broadway', 77, 'House C', 'West End', 'Fairview', '90504'),
            ('Union Road', 196, None, 'West End', 'Fairview', '90505'),
            ('Central Avenue', 9, None, 'East Side', 'Riverton', '90601'),
            ('Church Street', 230, 'Apt 8', 'East Side', 'Riverton', '90602'),
            ('College Road', 159, None, 'East Side', 'Riverton', '90603'),
            ('Market Street', 321, 'Store 1', 'East Side', 'Riverton', '90604'),
            ('River Avenue', 70, None, 'East Side', 'Riverton', '90605')]

    cursor.executemany(command, data)
    connection.commit()
    print('data entered.')

except mysql.connector.DatabaseError as error:
    print(error)
finally:
    cursor.close()
    connection.close()
