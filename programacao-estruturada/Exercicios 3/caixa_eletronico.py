def caixaEletronico(valor):
    notas = [1, 5, 10, 50, 100]
    notas.sort(reverse=True)
    for nota in notas:
        qtd = valor // nota
        if qtd > 0:
            print(f'{qtd} nota(s) de R${nota}')
            valor -= qtd * nota

valor = int(input('Digite o valor a ser sacado: '))
caixaEletronico(valor)