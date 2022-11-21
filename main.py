from models import Contact
from storage import read_contacts_from_csv, write_contact_to_csv
from utils import quick_sort


def main():
    ans = True
    while ans:
        print("""
      ******* Phone Directory Management System *******
      1.Insert new records
      2.Delete existing records
      3.Search a record by name
      4.Display records in sorted order
      5.Quit the system
      """)
        ans = input("What would you like to do? ")

        if ans == '1':
            print("insert new records:")

            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone: ")

            new_contact = Contact(name, address, phone)
            write_contact_to_csv(new_contact)

        elif ans == '2':
            print("delete records:")
            # Your code about how to delete existing records #

        elif ans == '3':
            print("search a record:")
           # Your code about how to search a record by name #

        elif ans == '4':
            contacts = read_contacts_from_csv()
            quick_sort(contacts, 0, len(contacts) - 1)
            for contact in contacts:
                print(contact)

        elif ans == '5':
            break

        else:
            print("Unknown Option Selected!")


if __name__ == '__main__':
    main()
