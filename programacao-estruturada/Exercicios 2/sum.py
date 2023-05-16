import math

def soma(n1, n2, n3):
    double = (n1*2) * (n2/2)
    triple = (n1*3) + n3
    cube = math.pow(n3, 3)
    print(f"o produto do dobro do primeiro com metade do segundo é: {double}")
    print(f"a soma do triplo do primeiro com o terceiro é: {triple}")
    print(f"o terceiro elevado ao cubo é: {cube}")
    return double, triple, cube

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
print(soma(n1, n2, n3))