def adicionarProduto(codigoProduto):
    nomeProduto = input('Qual o nome do produto: ')
    valorProduto = float(input('Qual o valor do produto: '))
    produtos.append({'codigo': codigoProduto, 'produto': nomeProduto, 'valor': valorProduto})
    
def removerProduto():
    produtoRemovido = input('Qual produto deseja remover?\n=> ')
    for item in produtos:
            if item['produto'] == produtoRemovido:
                produtos.remove(item)

def pesquisarProduto(codigoPesquisa):
    codigoPesquisa = int(input('Informe o codigo de pesquisa: '))
    for item in produtos:
            if item['codigo'] == codigoPesquisa:
                print(f"O produto selecionado:\nNome: {item['produto']}\nValor: R$ {item['valor']}")

produtos = []
choice = 0
codigoProduto = 0
while choice != 4:
    choice = int(input('O que deseja fazer?\n1 - adicionar produtor\n2 - remover produto\n3 - pesquisar produto\n4 - sair\n=> '))
    nomeProduto = ''
    valorProduto = 0
    if choice == 1:
        adicionarProduto(codigoProduto)
        codigoProduto = codigoProduto + 1
    elif choice == 2:
        produtoRemovido = ''
        removerProduto()
    elif choice == 3:
        codigoPesquisa = 0
        pesquisarProduto(codigoPesquisa)

print(f"\nLista de produtos\n")
for item in produtos:
    print(f"Produto:\n {item['produto']}, valor: R${item['valor']}\n")