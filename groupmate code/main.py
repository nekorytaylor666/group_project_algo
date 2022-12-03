from models import Contact
from storage import insert, delete


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

            name = input("Please Enter name: ")
            address = input("Enter email address: ")
            phone = input("Enter telephone number: ")

            insert_contact = Contact(name, address, phone)
            insert(insert_contact)

            print('Inserted')

        elif ans == '2':
            print("delete records:")

            name = input("Please at least enter name to delete: ")
            address = input("Enter address: ")
            phone = input("Enter telephone number: ")

            dele = Contact(name, address, phone)
            delete(dele)

            print('Deleted')
            # Your code about how to delete existing records #

        elif ans == '3':
            print("search a record:")
           # Your code about how to search a record by name #

        elif ans == '4':
            print("search a record:")

        elif ans == '5':
            break

        else:
            print("Unknown Option Selected!")


if __name__ == '__main__':
    main()
