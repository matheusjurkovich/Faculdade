quartoOcupado = int(input('Digite a quantidade de quartos ocupados:\n'))
quartoSimples = float(input('Digite o valor da diária do quarto simples:\n'))
quartoDuplo = float(input('Digite o valor da diária do quarto duplo:\n'))
alarme = float(input('Digite o valor do serviço de alarme:\n'))
totalHotel = 0

for i in range(quartoOcupado):
    tipoQuarto = int(
        input('Digite o tipo do quarto(1 - simples, 2 - duplo):\n'))
    alarmeQuarto = int(
        input('Digite a quantidade de serviços de alarme solicitada:\n'))
    valorConsumo = float(input('Digite o valor consumido no quarto:\n'))
    if (tipoQuarto == 1):
        valorQuarto = quartoSimples
    else:
        valorQuarto = quartoDuplo

    if (valorConsumo > (valorQuarto * 0.50) and valorConsumo <= (valorQuarto * 0.75)):
        desconto = 0.90
    elif (valorConsumo > (valorQuarto * 0.75) and valorConsumo <= (valorQuarto * 0.90)):
        desconto = 0.80
    elif (valorConsumo > (valorQuarto * 0.90)):
        desconto = 0.85
    else:
        desconto = 0

    valorTotal = (valorQuarto + (alarmeQuarto * alarme) + valorConsumo) - ((valorQuarto + (alarmeQuarto * alarme) + valorConsumo) * desconto)
    totalHotel = totalHotel + valorTotal
    print("Valor total do quarto: ", valorTotal)
    print("Valor bruto do quarto: ", valorQuarto +
          (alarmeQuarto * alarme) + valorConsumo)
    print("Desconto do quarto: ",
          ((valorQuarto + (alarmeQuarto * alarme) + valorConsumo) * desconto))

print("\n\n\nTotal de rendimento do hotel: ", totalHotel)
