def turnoDaAula(turno):
    newTurno = turno.upper()
    if newTurno == 'M':
        return 'Bom dia!'
    elif newTurno == 'V':
        return 'Boa tarde!'
    elif newTurno == 'N':
        return 'Boa noite!'
    else:
        return 'Turno inválido!'

turno = input('Digite o turno da aula: ')
print(turnoDaAula(turno))