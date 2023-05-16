def invertNumero(n1, n2):
    numeroA = n2
    numeroB = n1
    print(f"O numero A vale {numeroA} e o B vale {numeroB}")
    return numeroA, numeroB

invertNumero(int(input("Digite o valor A")), int(input("Digite o valor B")))