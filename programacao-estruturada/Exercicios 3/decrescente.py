listaDeNumeros = []

listaDeNumeros.append(int(input("Digite um número: ")))
listaDeNumeros.append(int(input("Digite outro número: ")))
listaDeNumeros.append(int(input("Digite mais um número: ")))

listaDeNumeros.sort(reverse=True)
print(listaDeNumeros)
for number in listaDeNumeros:
    print(number)