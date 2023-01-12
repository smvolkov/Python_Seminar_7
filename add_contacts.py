def add_contacts(choice, file):
    if choice == 1:
        with open(file, 'a', encoding="utf-8") as cl:
            cl.write('\n\n')
            cl.write(input('Введите фамилию: ') + '\n')
            cl.write(input('Введите имя: ') + '\n')
            cl.write(input('Введите телефон: ') + '\n')
            cl.write(input('Введите фамилию: '))
            
    if choice == 2:
        with open(file, 'a', encoding="utf-8") as c2:
            c2.write('\n')
            c2.write(input('Введите фамилию: ') + ', ')
            c2.write(input('Введите имя: ') + ', ')
            c2.write(input('Введите телефон: ') + ', ')
            c2.write(input('Введите фамилию: '))