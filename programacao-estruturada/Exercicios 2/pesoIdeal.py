def pesoIdeal(altura):
    sexualidade = input("Digite seu sexo (F ou M): ").upper()
    if sexualidade == "M":
        peso = (72.7 * altura) - 58
        return peso
    elif sexualidade == "f":
        peso = (62.1 * altura) - 44.7
        return peso
    elif sexualidade != "M" and sexualidade != "F":
        print("Digite uma sexualidade valida")


altura = float(input("Digite sua altura: "))
print(f"Seu peso ideal seria {pesoIdeal(altura)} kg")