def aumentoSalarial(salario):
    if salario >= 280:
        porcentagem = 20/100
        aumento = salario * porcentagem
        novoSalario = salario + aumento
        print(f"\nSeu salario antes do aumento é R${salario}\nO percentual de aumento é {porcentagem}%\nO aumento foi de R${aumento}\nSeu novo salario é R${novoSalario}\n")
        return novoSalario
    elif salario > 280 and salario <= 700:
        porcentagem = 15/100
        aumento = salario * porcentagem
        novoSalario = salario + aumento
        print(f"\nSeu salario antes do aumento é R${salario}\nO percentual de aumento é {porcentagem}%\nO aumento foi de R${aumento}\nSeu novo salario é R${novoSalario}\n")
        return novoSalario
    elif salario > 700 and salario <= 1500:
        porcentagem = 10/100
        aumento = salario * porcentagem
        novoSalario = salario + aumento
        print(f"\nSeu salario antes do aumento é R${salario}\nO percentual de aumento é {porcentagem}%\nO aumento foi de R${aumento}\nSeu novo salario é R${novoSalario}\n")
        return novoSalario
    elif salario > 1500:
        porcentagem = 5/100
        aumento = salario * porcentagem
        novoSalario = salario + aumento
        print(f"\nSeu salario antes do aumento é R${salario}\nO percentual de aumento é {porcentagem}%\nO aumento foi de R${aumento}\nSeu novo salario é R${novoSalario}\n")
        return novoSalario
    

salario = int(input("Digite o seu salário: "))
aumentoSalarial(salario)

