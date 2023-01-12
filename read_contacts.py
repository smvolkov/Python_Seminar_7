def open_contacts_txt(file, mode = 'r'):
    with open (file, mode, encoding="utf-8") as c1:
        return list(map(lambda c: c.replace('\n', ', '), c1.read().split('\n\n')))
    
def open_contacts_csv(file, mode = 'r'):
    with open (file, mode, encoding="utf-8") as c2:
        return list(map(lambda c: c.replace('\n', ''), c2.readlines()))
