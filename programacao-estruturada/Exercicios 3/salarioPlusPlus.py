def calculoDeSalario(salHora, hora):
    salario = salHora * hora
    if salario < 900:
        INSS = 10/100
        sindicato = 3/100
        FGTS = 11/100
        descontos = (salario * IR) + (salario * INSS) + (salario * sindicato)
        salarioLiquido = salario - descontos
        print(f"\nSalario bruto (R${salHora} * {hora}h): R${salario}\nINSS (10%): R${salario * INSS}\nFGTS (11%): R${salario * FGTS}\nSindicato (3%): R${salario * sindicato}\nDescontos: R${descontos}\nSalario liquido R${salarioLiquido}\n")
    elif salario > 900 and salario <= 1500:
        IR = 5/100
        INSS = 10/100
        sindicato = 3/100
        FGTS = 11/100
        descontos = (salario * IR) + (salario * INSS) + (salario * sindicato)
        salarioLiquido = salario - descontos
        print(f"\nSalario bruto (R${salHora} * {hora}h): R${salario}\nIR (5%): R${salario * IR}\nINSS (10%): R${salario * INSS}\nFGTS (11%): R${salario * FGTS}\nSindicato (3%): R${salario * sindicato}\nDescontos: R${descontos}\nSalario liquido R${salarioLiquido}\n")
    elif salario > 1500 and salario <= 2500:
        IR = 10/100
        INSS = 10/100
        sindicato = 3/100
        FGTS = 11/100
        descontos = (salario * IR) + (salario * INSS) + (salario * sindicato)
        salarioLiquido = salario - descontos
        print(f"\nSalario bruto (R${salHora} * {hora}h): R${salario}\nIR (10%): R${salario * IR}\nINSS (10%): R${salario * INSS}\nFGTS (11%): R${salario * FGTS}\nSindicato (3%): R${salario * sindicato}\nDescontos: R${descontos}\nSalario liquido R${salarioLiquido}\n")
    elif salario > 2500:
        IR = 20/100
        INSS = 10/100
        sindicato = 3/100
        FGTS = 11/100
        descontos = (salario * IR) + (salario * INSS) + (salario * sindicato)
        salarioLiquido = salario - descontos
        print(f"\nSalario bruto (R${salHora} * {hora}h): R${salario}\nIR (20%): R${salario * IR}\nINSS (10%): R${salario * INSS}\nFGTS (11%): R${salario * FGTS}\nSindicato (3%): R${salario * sindicato}\nDescontos: R${descontos}\nSalario liquido R${salarioLiquido}\n")

salHora = float(input("Digite o seu salário por hora: "))
hora = int(input("Digite a quantidade de horas trabalhadas: "))
calculoDeSalario(salHora, hora)