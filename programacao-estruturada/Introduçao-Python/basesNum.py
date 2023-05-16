def TransformarDEC(num): 
    binario = ''
    while(num > 0): 
        binario = str(num % 2) + binario
        num = num // 2
    return binario

print(TransformarDEC(int(input('Digite um número: '))))


