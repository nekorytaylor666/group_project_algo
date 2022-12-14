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

    def print_header(self):
        print(f"{bcolors.OKGREEN}{'Name':<50}|{'Address':<50}|{'Phone':<50}{bcolors.ENDC}")
        print(f"{'-' * 50}|{'-' * 50}|{'-' * 50}")
   
    def render_highlighted_contact(self, contact, match):
        matched_name = self.render_string(contact.name, match)
        print(f"{matched_name}|{contact.address:<50}|{contact.phone:<50}")
        

    def render_search_result_table(self, contacts, user_input):
        os.system('clear')
        self.print_header()
        for contact in contacts:
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
                # add extra width to result string to make it fit in cell since we added color to it and it will take more space
                extra_width += len(bcolors.OKGREEN) + len(bcolors.ENDC)
                
        
        return '{0: <{width}}'.format(result, width=self.cell_width + extra_width)

    def render_contact_table(self, contacts):
        self.print_header()
        for contact in contacts:
            self.render_contact(contact)

    def render_contact(self, contact):
        print(f"{contact.name:<50}|{contact.address:<50}|{contact.phone:<50}")
