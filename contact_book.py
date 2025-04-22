import json
import os

# File to store contacts
CONTACT_FILE = "my_contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        return []
    with open(CONTACT_FILE, "r") as f:
        return json.load(f)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact():
    print("\n📇 Add New Contact")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts = load_contacts()
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"✅ {name} has been added!")

# Show all contacts (names + phones only)
def show_all_contacts():
    print("\n📒 Contact List")
    contacts = load_contacts()
    if not contacts:
        print("No contacts saved yet!")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

# Search for a contact
def search_contact():
    keyword = input("\n🔍 Search by name or phone: ").lower()
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print(f"\n📌 Found Contact:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
            found = True
    if not found:
        print("❌ No contact matched.")

# Update a contact
def update_contact():
    show_all_contacts()
    try:
        num = int(input("\nEnter contact number to update: ")) - 1
        contacts = load_contacts()
        contact = contacts[num]
        print(f"\n✏️ Updating {contact['name']}")
        contact['name'] = input("New Name (leave blank to keep same): ") or contact['name']
        contact['phone'] = input("New Phone: ") or contact['phone']
        contact['email'] = input("New Email: ") or contact['email']
        contact['address'] = input("New Address: ") or contact['address']
        save_contacts(contacts)
        print("✅ Contact updated!")
    except (IndexError, ValueError):
        print("⚠️ Invalid contact number.")

# Delete a contact
def delete_contact():
    show_all_contacts()
    try:
        num = int(input("\nEnter contact number to delete: ")) - 1
        contacts = load_contacts()
        removed = contacts.pop(num)
        save_contacts(contacts)
        print(f"🗑️ Deleted {removed['name']}")
    except (IndexError, ValueError):
        print("⚠️ Invalid contact number.")

# Main menu
def main_menu():
    while True:
        print("\n======= 📱 Contact Manager =======")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Bye! Your contacts are safe.")
            break
        else:
            print("❌ Invalid choice. Try again!")

# Run the program
main_menu()
