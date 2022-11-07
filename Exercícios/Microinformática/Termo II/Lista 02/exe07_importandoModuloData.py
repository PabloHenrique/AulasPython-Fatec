'''
Faça um programa que leia uma data e determine se ela é válida, ou seja, verifique se o mês
está entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos,
e 28 dias em anos não bissextos.
Faça funções para validação e para verificar se o ano é bissexto.
'''

from moduloData import validaData, validaEntrada

while True:
    d = input('Entre com a data no formato dd/mm/aaaa >> ')
    if validaEntrada(d):
        break
    print('Entrada no formato inválido. Digite novamente...')
if validaData(d):
    print('Data válida!!')
else:
    print('Data inválida!!')