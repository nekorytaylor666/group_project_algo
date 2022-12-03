import csv
from models import Contact


def insert(contact):
    with open('allRecords.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, ['name', 'address', 'phone'])
        writer.writerow(
            {'name': contact.name, 'address': contact.address, 'phone': contact.phone})

def delete(dele):
    list=[]
    with open('allRecords.csv', newline='') as csvFile:
        reader = csv.DictReader(csvFile, ['name', 'address', 'phone'])
        for row in reader:
            if Contact(row['name'], row['address'], row['phone']) != dele:
                list.append(row)
        #print(list)

        with open('allRecords.csv', 'w', newline='') as csvFile:
            writer = csv.DictWriter(csvFile, ['name', 'address', 'phone'])
            writer.writerows(list)