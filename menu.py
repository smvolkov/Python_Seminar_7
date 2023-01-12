from read_contacts import open_contacts_txt
from read_contacts import open_contacts_csv
from view_contacts import print_contacts
from add_contacts import add_contacts
from update_contacts import update_contact
from write_updates import write_updates
from delete_contact import delete_contact
from exit import exit

# В меню осуществляется выбор действия и затем выбор справочника, в котором совершается действие
# menu() принимает номер пункта, который определяет, какой метод далее вызывается
# submenu() принимает номер файла, который определяет, с каким файлом работать, и передает его название в дальнейшие методы 

def menu():
    print(f'Выберите действие: \n 1. Открыть справочник контактов \n 2. Добавить контакт \n 3. Изменить контакт \n 4. Удалить контакт \n 5. Выход \n')
    p = int(input())
    if p == 5:
        exit()
    else:
        submenu(p)
    
def submenu(pp):
    f_name1 = 'contacts1.txt'
    f_name2 = 'contacts2.csv'
    print(f'Выберите справочник контактов: \n 1. {f_name1} \n 2. {f_name2} \n')
    c = int(input())
    if c == 1:
        f_name = f_name1
        c_list = open_contacts_txt(f_name)
    if c == 2:
        f_name = f_name2
        c_list = open_contacts_csv(f_name)
        
    if pp == 1:
        print_contacts(c_list, f_name)
    if pp == 2:
        add_contacts(c, f_name)
    if pp == 3:
        new_list = update_contact(c_list, f_name)
        write_updates(new_list, c, f_name)
    if pp == 4:
        new_list = delete_contact(c_list, f_name)
        write_updates(new_list, c, f_name)
        
        
  
menu()