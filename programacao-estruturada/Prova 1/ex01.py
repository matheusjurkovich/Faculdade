def validacao(numero):
    if numero >= 50 and numero <= 100:
        return True
    else:
        return False

numeros = []
for num in range(5):
    numberInput = int(input("Digite um numero: "))
    if numberInput > 0:
        numeros.append(numberInput)
        if numberInput < 50:
            print('Menor que 50')
        elif numberInput > 100:
            print('Maior que 100')
    else:
        print('Numero negativo')

media = filter(validacao, numeros)
mediaLista = list(media)
print(sum(mediaLista) / len(mediaLista))