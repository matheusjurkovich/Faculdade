def maiorNumero(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f"{n1} é maior que {n2} e {n3}")
        return n1
    elif n2 > n1 and n2 > n3:
        print(f"{n2} é maior que {n1} e {n3}")
        return n2
    else:
        print(f"{n3} é maior que {n1} e {n2}")
        return n3

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
maiorNumero(n1, n2, n3)
