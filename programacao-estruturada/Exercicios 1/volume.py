import math

def calculoDeVolume(raio, altura):
    volume = math.pi * (raio ** 2) * altura
    return volume
    

print(calculoDeVolume(float(input("Digite o raio: ")), float(input("Digite a altura: "))))