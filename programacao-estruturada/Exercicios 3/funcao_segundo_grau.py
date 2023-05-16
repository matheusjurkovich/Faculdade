def funcaoSegundoGrau(a, b, c):
    delta = (b**2) - (4*a*c)
    if delta < 0:
        return None
    else:
        x1 = (-b + delta**(1/2)) / (2*a)
        x2 = (-b - delta**(1/2)) / (2*a)
        return x1, x2

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
resultado = funcaoSegundoGrau(a, b, c)
if resultado == None:
    print('Não existe raiz')
else:
    print('x1 =', resultado[0])
    print('x2 =', resultado[1])
