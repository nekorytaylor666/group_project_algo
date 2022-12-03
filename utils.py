from renderer import ClientUI
from storage import read_contacts_from_csv


def quick_sort(contacts, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(contacts, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(contacts, low, pi - 1)
        quick_sort(contacts, pi + 1, high)


def partition(contacts, low, high):
    i = (low - 1)  # index of smaller element
    pivot = contacts[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if contacts[j].name <= pivot.name:
            # increment index of smaller element
            i = i + 1
            contacts[i], contacts[j] = contacts[j], contacts[i]

    contacts[i + 1], contacts[high] = contacts[high], contacts[i + 1]
    return (i + 1)


