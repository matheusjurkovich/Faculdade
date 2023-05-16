def notaAluno(media):
    if media >= 9:
        print("Nota A")
    elif media >= 7.5 and media < 9:
        print("Nota B")
    elif media >= 6 and media < 7.5:
        print("Nota C")
    elif media >= 4 and media < 6:
        print("Nota D")
    elif media < 4:
        print("Nota E")

def mediaAluno(nota1, nota2):
    media = (nota1 + nota2) / 2
    notaAluno(media)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
mediaAluno(nota1, nota2)