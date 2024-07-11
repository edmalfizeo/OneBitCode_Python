def add_contact(name, phone, email):
    with open('contacts.txt', 'a') as file:
        file.write(f'{name}, {phone}, {email}\n')


def list_contacts():
    with open('contacts.txt', 'r') as file:
        contacts = file.readlines()
        for contact in contacts:
            print(contact, end='')


def remove_contact(name):
    with open('contacts.txt', 'r') as file:
        contacts = file.readlines()
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            if name not in contact:
                file.write(contact)


