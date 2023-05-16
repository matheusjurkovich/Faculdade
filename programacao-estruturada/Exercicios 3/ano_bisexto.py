def bisexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    else:
        return False

ano = int(input('Digite um ano: '))
if bisexto(ano):
    print('É bisexto')
else:
    print('Não é bisexto')