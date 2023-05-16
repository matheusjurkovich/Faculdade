def calculoDeCombustivel(time, velocity):
    distance = time * velocity
    litrosUsados = distance / 12
    print(f"A velocidade média foi: {velocity}")
    print(f"A distancia foi: {distance}")
    print(f"O tempo gasto foi: {time}")
    print(f"O combustivel gasto foi: {litrosUsados}")

calculoDeCombustivel(float(input("Quanto tempo durou a viagem?")), int(input("Qual foi sua velocidade media?")))