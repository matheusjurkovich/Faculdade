def produtoBarato(preco1, preco2, preco3):
    if preco1 < preco2 and preco1 < preco3:
        print(f"{preco1} é o menor preço")
        return preco1
    elif preco2 < preco1 and preco2 < preco3:
        print(f"{preco2} é o menor preço")
        return preco2
    else:
        print(f"{preco3} é o menor preço")
        return preco3

preco1 = float(input("Digite o primeiro preço: "))
preco2 = float(input("Digite o segundo preço: "))
preco3 = float(input("Digite o terceiro preço: "))
produtoBarato(preco1, preco2, preco3)