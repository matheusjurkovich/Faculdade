def numeral(numero):
    if numero < 1000:
        centena = numero // 100
        dezena = (numero - (centena * 100)) // 10
        unidade = numero - (centena * 100) - (dezena * 10)
        print(f"O numero tem {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s).")
    else:
        return "O numero deve ser menor que 1000"

numero = int(input("Digite um numero menor que 1000: "))
numeral(numero)