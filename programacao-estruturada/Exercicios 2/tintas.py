import math

def tinta(metros):
    lataQuantidade = round(metros) / 54
    lataValor = lataQuantidade * 80
    print(f"O orçamento é: {lataQuantidade} latas de tinta R${lataValor}")
    return lataQuantidade, lataValor

metrosQuadrados = int(input("Quantos metros quadrados deseja pintar: "))
tinta(metrosQuadrados)


    

    
