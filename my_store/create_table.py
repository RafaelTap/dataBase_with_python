from connection import connection, cursor

try:
    cursor.execute(
        ''' CREATE TABLE IF NOT EXISTS product(
            code SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price NUMERIC(10,2) NOT NULL);
        ''')

    # just in case: to create table is not necessary make commit.
    connection.commit()
    print('table created')
except Exception as err:
    print(err)

