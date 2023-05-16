import datetime

def data_valida(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

data = input('Digite uma data no formato dd/mm/aaaa: ')
if data_valida(data):
    print(f'Data válida {data}')
else:
    print('Data inválida')