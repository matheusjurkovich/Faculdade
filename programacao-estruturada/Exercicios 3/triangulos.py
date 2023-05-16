def triangulo(a, b, c):
    if a + b >= c:
        triangulo = True
        print('É um triângulo')
    else:
        triangulo = False
        print('Não é um triângulo')
    if triangulo == True:
        if a == b and b == c:
            print('Triângulo equilátero')
        elif a == b or b == c or a == c:
            print('Triângulo isósceles')
        else:
            print('Triângulo escaleno')
    else:
        print('Erro? o besta do programador não sabe programar')

a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))
triangulo(a, b, c)
    