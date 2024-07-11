from contact_book import *


def main():
    while True:
        print('1. Add contact')
        print('2. List contacts')
        print('3. Remove contact')
        print('4. Exit')
        option = input('Choose an option: ')
        if option == '1':
            name = input('Name: ')
            phone = input('Phone: ')
            email = input('Email: ')
            add_contact(name, phone, email)
        elif option == '2':
            list_contacts()
        elif option == '3':
            name = input('Name: ')
            remove_contact(name)
        elif option == '4':
            break
        else:
            print('Invalid option')


main()
