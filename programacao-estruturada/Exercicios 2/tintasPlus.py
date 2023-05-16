import math

def tintaGrande(metros):
    latas = math.ceil(metros/108)
    preco = latas*80
    print("Você precisará de {} latas de tinta grande, que custará R${}".format(latas, preco))

def tintaPequena(metros):
    latas = math.ceil(metros/21.6)
    preco = latas*25
    print("Você precisará de {} latas de tinta pequena, que custará R${}".format(latas, preco))

def tinta(metros):
    tipoLata = int(input("Informe o tamanho da lata\n1- Grande\n2-Pequena\n3-Misturar\n:"))
    if tipoLata == 1:
        tintaGrande(metros)
    elif tipoLata == 2:
        tintaPequena(metros)
    elif tipoLata == 3:
        while metros > 0:
            qtd = metros // 108
            if qtd > 0:
                tintaGrande(qtd*108)
                metros -= qtd*108
            else:
                tintaPequena(metros)
                metros -= metros
    

metrosQuadrados = int(input("Quantos metros quadrados deseja pintar: "))
tinta(metrosQuadrados)