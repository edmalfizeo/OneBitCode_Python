class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'Name: {self.name}, Phone: {self.phone}, Email: {self.email}'


class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)

    def show_all(self):
        if not self._contacts:
            print("No contacts found.")
        else:
            for contact in self._contacts:
                print(contact)

    def delete(self, name):
        found = False

        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                print(f'Contact {name} deleted.')
                found = True
                break
        if not found:
            print('Contact not found')

    def search(self, name):
        found = False

        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                found = True
                break
        if not found:
            print('Contact not found')
