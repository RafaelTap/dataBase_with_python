from connection import connection, cursor
from psycopg2 import Error
from faker import Faker

class AppDB:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect_to_db()

    def connect_to_db(self):
        self.connection = connection
        self.cursor = cursor
        print('you are connected to data base')

#READ
    def product_list(self):
        try:
            self.cursor.execute("""SELECT * FROM product GROUP BY code""")
            product_list = self.cursor.fetchall()
            for product in product_list:
                print(product)
        except (Exception, Error) as err:
            print(err)
            return []


#CREATE
    def insert_product(self, name, price):
        try:
            self.cursor.execute("""INSERT INTO product(name, price) 
                                   VALUES (%s, %s)""", (name, price))
            self.connection.commit()
            print('product inserted')
        except (Exception, Error) as err:
            print(err)

#UPDATE
    def update_product(self, product_id,  name, price):
        try:
            self.cursor.execute("""UPDATE product SET name = %s, price = %s
                                   WHERE code = %s """, (product_id, name, price))
            self.connection.commit()
            print('product up to date')
        except (Exception, Error) as err:
            print(err)

#DELETE
    def delete_product(self, product_id):
        try:
            self.cursor.execute("""DELETE FROM product
                               WHERE code = %s""",(product_id,))
            self.connection.commit()
            print('product deleted')
        except (Exception, Error) as err:
            print(err)

if __name__ == '__main__':
    appDB = AppDB()
    fk = Faker('PT_BR')
    appDB.product_list()


    """for _ in range(10):
        name = fk.word()
        price = round(fk.random_number(digits=5) / 100, 2)
        appDB.insert_product(name, price)"""