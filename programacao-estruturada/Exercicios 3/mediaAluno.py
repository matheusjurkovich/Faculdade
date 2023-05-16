def mediaAluno(n1, n2):
    media = (n1 + n2) / 2
    if media >= 7 and media < 10:
        print(f"A média do aluno é {media}. Parabéns!")
    elif media < 7:
        print(f"A média do aluno é {media}. Reprovado!")
    elif media == 10:
        print(f"A média do aluno é {media}. Aprovado com Distinção!")
    else:
        print("Erro")

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
mediaAluno(nota1, nota2)  
