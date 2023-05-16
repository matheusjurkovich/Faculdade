def positiveOrNegative(numero):
    if numero > 0:
        print(f"{numero} é positivo")
        return 'Positivo'
    elif numero < 0:
        print(f"{numero} é negativo")
        return 'Negativo'
    else:
        print('O número é 0')
        return '0'

numero = int(input("Digite um número: "))
positiveOrNegative(numero)