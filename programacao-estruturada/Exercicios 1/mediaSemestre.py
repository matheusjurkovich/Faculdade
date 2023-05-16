def media(n1, n2, p):
    mediaNota = (n1 * 3 + n2 * 3 + p * 4) / 10
    print(f"Seu média semestral foi: {mediaNota}")
    return mediaNota

media(int(input("Digite a primeira nota: ")), int(input("Digite a segunda nota: ")), int(input("Não sei oq é p so digita ai: ")))