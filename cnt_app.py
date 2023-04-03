from tinydb import TinyDB, Query
import black

db = TinyDB('db.json')
contacts = db.table('contacts')

def add_contact():
    name = input('Enter name: ')
    email = input('Enter email: ')
    phone = input('Enter phone number: ')
    contacts.insert({'name': name, 'email': email, 'phone': phone})
    print('Contact added successfully!')

def show_contacts():
    all_contacts = contacts.all()
    for contact in all_contacts:
        print(contact)

def edit_contact():
    name = input('Enter name of the contact to edit: ')
    contact = Query()
    result = contacts.search(contact.name == name)
    if result:
        new_name = input('Enter new name (leave blank to keep current name): ')
        new_email = input('Enter new email (leave blank to keep current email): ')
        new_phone = input('Enter new phone number (leave blank to keep current phone number): ')
        update_fields = {}
        if new_name != '':
            update_fields['name'] = new_name
        if new_email != '':
            update_fields['email'] = new_email
        if new_phone != '':
            update_fields['phone'] = new_phone
        contacts.update(update_fields, contact.name == name)
        print('Contact updated successfully!')
    else:
        print('Contact not found.')

def remove_contact():
    name = input('Enter name of the contact to remove: ')
    contact = Query()
    result = contacts.remove(contact.name == name)
    if result:
        print('Contact removed successfully!')
    else:
        print('Contact not found.')

def main():
    while True:
        print('\nContact Book\n')
        print('1. Add Contact')
        print('2. Show Contacts')
        print('3. Edit Contact')
        print('4. Remove Contact')
        print('5. Exit')
        choice = input('\nEnter your choice: ')
        if choice == '1':
            add_contact()
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            remove_contact()
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
