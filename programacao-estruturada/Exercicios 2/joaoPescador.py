def calculoMultaKg(quilogramas):
    if quilogramas > 50:
        novo_peso = quilogramas - 50
        multa = novo_peso * 4
        print(f"Voce deve pagar R${multa} de multa!")
    else:
        print("Voce nao precisa pagar nada!")
    
quilogramas = float(input("Quantos quilos de peixe voce pescou: "))
calculoMultaKg(quilogramas)
    