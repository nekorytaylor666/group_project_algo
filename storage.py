import csv

from models import Contact


def write_contact_to_csv(contact):
    with open('phone_dictionary.csv', mode='a') as csv_file:
        fieldnames = ['name', 'address', 'phone']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(
            {'name': contact.name, 'address': contact.address, 'phone': contact.phone})

# function to read all contacts from csv to array


def read_contacts_from_csv():
    contacts = []
    with open('phone_dictionary.csv', mode='r') as csv_file:
        fieldnames = ['name', 'address', 'phone']
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        # skip header
        next(reader)

        for row in reader:

            contact = Contact(row['name'], row['address'], row['phone'])
            contacts.append(contact)
    return contacts

# function to delete contact from csv


def delete_contact_from_csv(contact):
    contacts = read_contacts_from_csv()
    contacts.remove(contact)
    with open('phone_dictionary.csv', mode='w') as csv_file:
        fieldnames = ['name', 'address', 'phone']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(
                {'name': contact.name, 'address': contact.address, 'phone': contact.phone})
