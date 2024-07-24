import uuid

class Contact:
    def __init__(self, id, store_name, phone_number, email, address):
        self.id = id
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def update(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __repr__(self):
        return f"ID: {self.id} | Store Name: {self.store_name} | Phone: {self.phone_number} | Email: {self.email} | Address: {self.address}"

contacts = []
id_counter = 0

def add_contact():
    global id_counter
    id_counter += 1
    store_name = input("Enter store name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(id_counter, store_name, phone_number, email, address)
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts available.")

def search_contacts():
    query = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if query.lower() in contact.store_name.lower() or query in contact.phone_number]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(contact)
    else:
        print("No contacts found.")

def update_contact():
    contact_id = int(input("Enter the contact ID to update: "))
    for contact in contacts:
        if contact.id == contact_id:
            store_name = input("Enter new store name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact.update(store_name, phone_number, email, address)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    contact_id = int(input("Enter the contact ID to delete: "))
    global contacts
    contacts = [contact for contact in contacts if contact.id != contact_id]
    print("Contact deleted successfully!")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
