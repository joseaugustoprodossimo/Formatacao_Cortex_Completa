def Retornar_Ultimo_Nome(item):
    item = item.split(' ')

    if(len(item) > 1):
        return item[len(item) - 1]
    elif(len(item) == 1):
        return item[0]
    else:
        ""

def Remover_Caracteres_Especiais(item):
    if item:
        return ''.join(char for char in item if char.isalnum())
    else:
        ''

def Formatar_sites(item):
    item = str(item)
    
    if(len(item) > 5):
        return item.replace('http://', '').replace('https://', '').replace('www.', '')
    else:
        ""

def Retornar_Cargo(item):

    item = str(item)

    item = item.split('-')

    if(len(item) == 2):
        return item[1]
    elif(len(item) == 3):
        return item[1] + ' ' + item[2]
    else:
        return ""

