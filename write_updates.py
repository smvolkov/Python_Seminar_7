def write_updates(cont_list, separator, file):
    if separator == 1:
        sep = '\n'
    if separator == 2:
        sep = ', '        
        
    new_cont = ''
    for i in cont_list:
        sp = i.split(", ")
        for j in range(len(sp)):
            new_cont = new_cont + sp[j] + sep
            if j == len(sp) - 1:
                if separator == 2:
                    new_cont = new_cont[:-2]
                new_cont = new_cont + '\n'
        with open (file, 'w+', encoding="utf-8") as nc:
            nc.write(new_cont.rstrip())
            
            
