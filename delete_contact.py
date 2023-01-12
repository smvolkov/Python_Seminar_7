from view_contacts import print_contacts

def delete_contact(contacts_list, file):
    print_contacts(contacts_list, file)
    cn = int(input('Какой контакт удалить (введите номер строки): '))
    contacts_list.pop(cn-1)
    
    return contacts_list
