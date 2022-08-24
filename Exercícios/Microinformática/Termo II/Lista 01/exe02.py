'''
    Faça  um  programa  em Python que  leia  uma  frase  e imprima  quantas vogais tem  esta  frase.
    Considerar minúscula e maiúscula.
'''

from unidecode import unidecode

frase = input('Informe uma frase >>> ')

qt_vogais = 0

for i in frase:
    if 'A' in i.upper():
        qt_vogais += 1
    elif 'E' in i.upper():
        qt_vogais += 1
    elif 'I' in i.upper():
        qt_vogais += 1
    elif 'O' in i.upper():
        qt_vogais += 1
    elif 'U' in i.upper():
        qt_vogais += 1

print(f'Essa frase tem {qt_vogais} vogais')

print('='*50)

frase = input('Informe uma frase >>> ')

qt_vogais = 0

qt_vogais += frase.upper().count('A')
qt_vogais += frase.upper().count('E')
qt_vogais += frase.upper().count('I')
qt_vogais += frase.upper().count('O')
qt_vogais += frase.upper().count('U')

print(f'Essa frase tem {qt_vogais} vogais')

print('='*50)

frase = input('Informe uma frase >>> ')

qt_vogais = 0

for i in frase.upper():
    if i in 'AEIOU':
        qt_vogais

print(f'Essa frase tem {qt_vogais} vogais')

print('='*50)

frase = input('Informe uma frase >>> ')

qt_vogais = 0

for i in unidecode(frase).upper():
    if i in 'AEIOU':
        qt_vogais

print(f'Essa frase tem {qt_vogais} vogais')
