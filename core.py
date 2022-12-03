from renderer import ClientUI
from storage import read_contacts_from_csv


def search(): 
    print("search a record:")
    # read all contacts from csv file
    contacts = read_contacts_from_csv()
    # get the name of the contact to search
    user_input = input("Enter name: ") 
    # if the name is empty we display all contacts
    if user_input == '':
        ClientUI().render_contact_table(contacts)
        return
    # if the name is not empty we search for the contact
    result = []
    # linear search
    for contact in contacts:
        if user_input in contact.name:
            result.append(contact)
    # display the result 
    ClientUI().render_search_result_table(result, user_input)
    return