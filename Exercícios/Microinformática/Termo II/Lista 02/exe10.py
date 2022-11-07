'''
10. Faça um programa que calcule as raízes da equação de 2o grau
'''
from math import sqrt

def calculaDelta():
    return b * b - 4 * a * c

def calculaRaizes(delta):
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    return x1, x2

print('Informe os coeficientes de uma equação de 2º grau')
a = float(input('a >> '))
if a == 0:
    print('Não é equação de 2º grau')
else:
    b = float(input('b >> '))
    c = float(input('c >> '))
    delta = calculaDelta()
    if delta < 0:
        print('Não existe raiz real')
    else:
        x1, x2 = calculaRaizes(delta)
        if delta == 0:
            print(f'Existe uma raiz >> x = {x1}')
        else:
            print(f'Existem 2 raízes >> x1 = {x1} e x2 = {x2}')
