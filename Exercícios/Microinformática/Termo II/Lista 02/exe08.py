'''
Faça um programa para entrar com a data de nascimento, data atual e mostrar a idade da
pessoa. Utilize as funções do exercício anterior para validar a entrada das datas.
'''
from moduloData import *

def entraData(texto):
    while True:
        data = input(f'Informe a {texto} no formato dd/mm/aaaa >> ')
        if validaEntrada(data) and validaData(data):
            return data
        print('Data inválida!! Digite novamente...')

dNasc = entraData('data de nascimento')
dAtual = entraData('data atual')
dn, mn, an = dNasc.split('/')
da, ma, aa = dAtual.split('/')
dn, mn, an = int(dn), int(mn), int(an)
da, ma, aa = int(da), int(ma), int(aa)
idade = aa - an
if mn > ma:
    idade -= 1
elif mn == ma and dn > da:
    idade -=1
print(f'Você tem {idade} anos')
