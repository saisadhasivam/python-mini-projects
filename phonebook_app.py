"""
Phonebook App - A simple command-line contact manager using a dictionary.

Features:
- Add a contact
- Search for a contact
- Delete a contact
- View all contacts
"""

# Dictionary to store phonebook contacts
phonebook = {}

# Menu loop
while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        name = input("Enter name: ").strip().capitalize()
        number = input("Enter number: ").strip()
        email = input("Enter email: ").strip()
        phonebook[name] = {"number": number, "email": email}
        print("Contact added!")

    elif choice == "2":
        name = input("Enter name you want to search: ").strip().capitalize()
        if name in phonebook:
            contact = phonebook[name]
            print(f"Name: {name} | Number: {contact['number']} | Email: {contact['email']}")
        else:
            print(f"{name} is not available in the contact list.")
    
    elif choice == "3":
        name = input("Enter the name you want to delete: ").strip().capitalize()
        if name in phonebook:
            del phonebook[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"{name} not found in contacts.")

    elif choice == "4":
        if not phonebook:
            print("No contacts to display.")
        else:
            print("\nAll Contacts:")
            for i, (name, contact) in enumerate(phonebook.items(), start=1):
                print(f"{i}. Name: {name} | Number: {contact['number']} | Email: {contact['email']}")
    
    elif choice == "5":
        print("Exiting Phonebook App.")
        break

    else:
        print("Invalid choice. Please try again.")
