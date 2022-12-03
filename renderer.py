# create class renderer
# create method render_menu
# create method render_contact_table
# create method render_contact
# create method render_contact_form

# create class renderer
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ClientUI:
    cell_width = 50
    def render_menu(self):
        print("""
        ******* Phone Directory Management System *******
        1.Insert new records
        2.Delete existing records
        3.Search a record by name
        4.Display records in sorted order
        5.Quit the system
        """)

    # create method render_contact_table
    def render_contact_table(self, contacts):
        # display contact table in beatiful table
        print(f"{bcolors.OKGREEN}{'Name':<50}|{'Address':<50}|{'Phone':<50}{bcolors.ENDC}")
        print(f"{'-' * 50}|{'-' * 50}|{'-' * 50}")
        for contact in contacts:
            self.render_contact(contact)
    
    # create method that will render contact table with width of symbols and fill with spaces if needed
    def render_contact(self, contact):
        print(f"{contact.name:<50}|{contact.address:<50}|{contact.phone:<50}")

    def render_highlighted_contact(self, contact, match):
        matched_name = self.render_string(contact.name, match)
        print(f"{matched_name}|{contact.address:<50}|{contact.phone:<50}")
        

    def render_search_result_table(self, contacts, user_input):
        os.system('clear')
        print(f"{bcolors.OKGREEN}{'Name':<50}{'Address':<50}{'Phone':<50}{bcolors.ENDC}")
        print(f"{'-' * 50}|{'-' * 50}|{'-' * 50}")
        for contact in contacts:
            # print contact if contact user_input contains user input
            if user_input in contact.name:
                self.render_highlighted_contact(contact, user_input) 
            
    def render_string(self, string, match):
        tmp = string.split(match)
        result = ''
        extra_width = 0
        for i in range(len(tmp)):
            if i == len(tmp) - 1:
                result += tmp[i]
            else:
                result += tmp[i] + bcolors.OKGREEN + match + bcolors.ENDC
                extra_width += len(bcolors.OKGREEN) + len(bcolors.ENDC)
                
        
        return '{0: <{width}}'.format(result, width=self.cell_width + extra_width)
