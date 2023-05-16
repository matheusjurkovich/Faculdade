def calculoSalario(salHora, hora):
    salBruto = salHora * hora
    ir = salBruto * 0.11
    inss = salBruto * 0.08
    sindicato = salBruto * 0.05
    salLiquido = salBruto - ir - inss - sindicato
    return salLiquido

salHora = int(input("Digite o valor do seu salário por hora: "))
horas = int(input("Digite a quantidade de horas trabalhadas: "))
print(f"Seu salário é de R${calculoSalario(salHora, horas)}")