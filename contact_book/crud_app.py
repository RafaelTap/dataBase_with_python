import psycopg2 as connector

def connect_to_db():
    try:
        connection = connector.connect(database='contactbook_db',
                                       user='postgres',
                                       password='rafael@dev',
                                       host='localhost'
                                       )
        return connection
    except connector.Error as err:
        print(err)
        return None

def create_contact(name, cellphone_number):
    connection = connect_to_db()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute('''INSERT INTO agenda (name, cellPhone_number) 
                                    VALUES (%s, %s) RETURNING contact_id''', (name, cellphone_number))
            contact_id = cursor.fetchall()[0]
            connection.commit()
            print(f"contact added: ID={contact_id}")
        except connector.Error as err:
            print(err)
        finally:
            cursor.close()
            connection.close()

def read_contacts():
    connection = connect_to_db()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute('''SELECT contact_id, name, cellPhone_number FROM agenda''')
            agenda_list = cursor.fetchall()
            for contact in agenda_list:
                print(f'contact_id: {contact[0]}, name: {contact[1]}, contact number: {contact[2]}')
        except connector.Error as err:
            print(err)
        finally:
            cursor.close()
            connection.close()

def update_contact(contact_id, new_name, new_number):
    connection = connect_to_db()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(''' UPDATE agenda 
                               SET name = %s, 
                               cellPhone_number = %s
                               WHERE contact_id = %s''', (new_name, new_number, contact_id))
            connection.commit()
            print('contact updated')
        except connector.Error as err:
            print(err)
        finally:
            cursor.close()
            connection.close()

def delete_contact(contact_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    if connection is not None:
        try:
            cursor.execute('''DELETE FROM agenda
                              WHERE contact_id = %s''', (contact_id,))
            connection.commit()
            print('contact deleted')
        except connector.Error as err:
            print(err)
        finally:
            cursor.close()
            connection.close()

def main():
    while True:
        action = input('<<<choose an action>>>\n'
                   '1: create contact\n'
                   '2: contacts list\n'
                   '3: update a contact\n'
                   '4: delete a contact\n')
        if action == '1':
            name = input('name: ')
            cellphone_number = input('cell phone number: ')
            create_contact(name, cellphone_number)
        elif action == '2':
            print('<<<contact list>>>\n')
            read_contacts()
        elif action == '3':
            contact_id = input('contact id: ')
            new_name = input('new name: ')
            new_number = input('new number: ')
            update_contact(contact_id, new_name, new_number)
        elif action == '4':
            contact_id = input('type contact id: ')
            delete_contact(contact_id)
            break
        else:
            print('no action selected')

if __name__ == '__main__':
    main()