def diasDaSemana(dia):
    if dia == 1:
        return 'Domingo'
    elif dia == 2:
        return 'Segunda'
    elif dia == 3:
        return 'Terça'
    elif dia == 4:
        return 'Quarta'
    elif dia == 5:
        return 'Quinta'
    elif dia == 6:
        return 'Sexta'
    elif dia == 7:
        return 'Sábado'
    else:
        return 'Dia inválido'

dia = int(input('Digite um número de 1 a 7: '))
print(diasDaSemana(dia))