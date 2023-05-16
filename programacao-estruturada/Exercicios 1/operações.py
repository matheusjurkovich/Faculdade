def operacoes(n1, n2):
    operacao = input("Qual operação deseja fazer: ")
    if operacao == "+":
        return n1 + n2
    elif operacao == "-":
        return n1 - n2
    elif operacao == "*":
        return n1 * n2
    elif operacao == "/":
        return n1 / n2

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

print(operacoes(numero1, numero2))