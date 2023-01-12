# Запись обновленного файла с измененным или удаленным контактом

def write_updates(cont_list, separator, file):
    if separator == 1: # Определяет формат файла и, исходя из этого, выбирается разделитель
        sep = '\n'
    if separator == 2:
        sep = ', '        
        
    new_cont = '' # Обновленный файл
    for i in cont_list: # Заполнение обновленного файла
        sp = i.split(", ")
        for j in range(len(sp)):
            new_cont = new_cont + sp[j] + sep
            if j == len(sp) - 1:
                if separator == 2:
                    new_cont = new_cont[:-2] # Убирает лишние запятые (', ') в конце строки для .csv файла
                new_cont = new_cont + '\n'
        with open (file, 'w+', encoding="utf-8") as nc: # Перезапись файла
            nc.write(new_cont.rstrip())
            
            
