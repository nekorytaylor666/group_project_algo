# generate 100 contacts

from models import Contact
from storage import write_contact_to_csv
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_phone():
    return ''.join(random.choice(string.digits) for i in range(10))


def generate_random_address():
    return generate_random_string(10) + ' ' + generate_random_string(10)


def generate_random_contact():
    name = generate_random_string(10)
    address = generate_random_address()
    phone = generate_random_phone()
    return Contact(name, address, phone)


def generate_100_contacts():
    for i in range(100):
        contact = generate_random_contact()
        write_contact_to_csv(contact)


if __name__ == '__main__':
    generate_100_contacts()
