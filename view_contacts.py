import read_contacts
from read_contacts import open_contacts_txt
from read_contacts import open_contacts_csv

def print_contacts(cont, name):
    print(f'Справочник {name}: ')
    for i in enumerate(cont, 1):
        print(i)