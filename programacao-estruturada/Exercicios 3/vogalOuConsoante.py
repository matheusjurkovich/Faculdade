def vogalOuConsoante(letra):
    newLetter = letra.lower()
    if newLetter == 'a' or newLetter == 'e' or newLetter == 'i' or newLetter == 'o' or newLetter == 'u':
        print(f"{newLetter} é uma vogal")
        return 'vogal'
    else:
        print(f"{newLetter} é uma consoante")
        return 'consoante'
    
letra = input("Digite uma letra: ")
vogalOuConsoante(letra)