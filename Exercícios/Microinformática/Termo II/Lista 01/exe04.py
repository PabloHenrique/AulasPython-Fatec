'''
    Faça um programa em Python que leia uma String e a escreva invertido.
'''

frase = input('Informe uma frase >>> ')

qt_caract = len(frase)
engrenagem_1 = qt_caract
engrenagem_2 = 0

if qt_caract%2 == 0:
    rodadas = qt_caract / 2
else:
    rodadas = (qt_caract-1) / 2

for i in range(rodadas):

