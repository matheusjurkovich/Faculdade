def speedUp(velocity, acceleration): 
    return velocity + acceleration

velocity = float(input('Digite a velocidade: ')) #input é uma função que permite que o usuário digite um valor
acceleration = float(input('Digite a aceleração: ')) #input é uma função que permite que o usuário digite um valor

print('Sua velocidade acelererada é: ', speedUp(velocity, acceleration)) #soma os valores digitados pelo usuário, convertendo-os para inteiros, para concatenar com a mensagem, usamos a vírgula

