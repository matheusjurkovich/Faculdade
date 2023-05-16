def calculoSalario(salario, aulas, porcentagem):
    mediaSalario = salario / aulas
    porcentagem = porcentagem / 100
    salarioFinal = salario + (salario * porcentagem)
    print(f"O salario final é: {salarioFinal}")
    return salarioFinal

calculoSalario(float(input("Digite o salario: ")), int(input("Digite o numero de aulas: ")), float(input("Digite a porcentagem do INSS: ")))
