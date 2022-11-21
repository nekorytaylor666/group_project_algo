class Contact:
    name = ''
    address = ''
    phone = ''

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f'{self.name}, {self.address}, {self.phone}'

    def __repr__(self):
        return f'{self.name} {self.address} {self.phone}'

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):

        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def __le__(self, other):
        return self.name <= other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)
