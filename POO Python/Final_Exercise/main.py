from classes import ContactBook


def main():
    contact_book = ContactBook()

    while True:
        option = int(input('''    
[1] Add contact
[2] Show contacts
[3] Search contact
[4] Delete contact
[5] Exit
Choose an option: '''))

        match option:
            case 1:
                name = input('Name: ')
                phone = input('Phone: ')
                email = input('Email: ')
                contact_book.add(name, phone, email)
            case 2:
                contact_book.show_all()
            case 3:
                name = input('Name: ')
                contact_book.search(name)
            case 4:
                name = input('Name: ')
                contact_book.delete(name)
            case 5:
                break
            case _:
                print('Invalid option')
                continue


main()

