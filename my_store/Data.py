from faker import Faker
from connection import connection, cursor

fk = Faker('PT_BR')

for _ in range(10):
    name = fk.word()
    price = round(fk.random_number(digits=5) / 100,2)
    print(name, price)
    cursor.execute('''INSERT INTO product (name, price) VALUES (%s, %s)''', (name, price))

connection.commit()
print('done')
cursor.close()
connection.close()


