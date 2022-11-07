'''
Elabore um programa em Python que lê uma String e calcule e imprima um código utilizando a
seguinte regra: para cada vogal, somar 5 pontos, para cada consoante somar 10 pontos,
desconsiderando qualquer outro caractere.
Exemplo: Linguagem de Programação
10 vogais (lembre-se de considerar vogais acentuadas) → 10 x 5 = 50
12 consoantes → 12 x 10 = 120
Código = 170
'''
from unidecode import unidecode

frase = input('Informe a frase >> ')
f = unidecode(frase).upper()
cod = 0
for carac in f:
    if carac.isalpha():
        if carac in 'AEIOU':
            cod += 5
        else:
            cod += 10
print(f'Código >> {cod}')

