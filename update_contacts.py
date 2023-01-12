from read_contacts import open_contacts_txt
from read_contacts import open_contacts_csv
from view_contacts import print_contacts

def update_contact(contacts_list, file):
    print_contacts(contacts_list, file)
    cn = int(input('Какой контакт изменить (введите номер строки): '))
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    description = input('Введите описание: ')
    new_line = f'{surname}, {name}, {phone}, {description}'
    contacts_list[cn-1] = new_line
    
    return contacts_list