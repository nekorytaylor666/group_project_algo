from renderer import ClientUI
from storage import read_contacts_from_csv


def search(): 
    print("search a record:")
    contacts = read_contacts_from_csv()
    # create infinite loop which will listen to user input and exit when user enters ':q'
    user_input = input("Enter name (type :q to leave!): ") 
    if user_input == '':
        ClientUI().render_contact_table(contacts)
        return

    result = []
    for contact in contacts:
        if user_input in contact.name:
            result.append(contact)
    
    ClientUI().render_search_result_table(result, user_input)
    return