def meterToCentimeter(metros):
    centimetros = metros * 100
    return centimetros

centimetros = int(input("Digite a quantidade de metros: "))
print(meterToCentimeter(centimetros))
print(f"{centimetros} metros equivalem a {meterToCentimeter(centimetros)} centimetros")
