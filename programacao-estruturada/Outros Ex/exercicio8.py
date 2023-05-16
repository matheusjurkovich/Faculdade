estoque = []
choice = 0
codigo = 1
while choice != 4:
    choice = int(input(
        "Selecione sua opção:\n1 - Adicionar Livro\n2 - Consultra Livro\n3 - Inventario\n4 - Sair\n=> "))
    if choice == 1:
        autor = input("Qual o nome do autor: ")
        title = input("Qual o nome do livro: ")
        editor = input("Qual a editora: ")
        year = int(input("Qual o ano de publicação: "))
        quantidade = int(input("Quantidade de livros: "))
        valor = float(input("Valor do livro: "))
        estoque.append({
            "registro": codigo,
            "autor": autor,
            "titulo": title,
            "editora": editor,
            "ano": year,
            "quantidade": quantidade,
            "valor": valor
        })
        codigo = codigo + 1
    elif choice == 2:
        codigoDoItem = int(input("Digite o codigo do livro: "))
        encontrado = False
        for item in estoque:
            if item["registro"] == codigoDoItem:
                encontrado = True
                break
        if encontrado == True:
            print(f"\nCodigo do livro: {item['registro']}\nAutor do livro: {item['autor']}\nTitulo do Livro: {item['titulo']}\nEditora: {item['editora']}\nAno de publicação: {item['ano']}\nQuantidade de unidades: {item['quantidade']}\nValor do livro: {item['valor']}\n")
        else:
            print("\nLivro não encontrado\n")
    elif choice == 3:
        print("Estoque:")
        for item in estoque:
            print(f"Autor do livro: {item['autor']}\nTitulo do Livro: {item['titulo']}\nEditora: {item['editora']}\nAno de publicação: {item['ano']}\nQuantidade de unidades: {item['quantidade']}\nValor do livro: {item['valor']}\n")