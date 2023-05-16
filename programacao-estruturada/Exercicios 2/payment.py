def calculoSalario(salHora, horas):
    salario = salHora * horas
    return salario

salario = int(input("Digite o valor do seu salário por hora: "))
horas = int(input("Digite a quantidade de horas trabalhadas: "))
print(f"Seu salário é de R${calculoSalario(salario, horas)}")