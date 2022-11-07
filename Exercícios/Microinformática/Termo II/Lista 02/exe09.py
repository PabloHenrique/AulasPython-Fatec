'''
9.	Faça um programa que receba a data atual e exiba-a na tela
no formato textual por extenso. Exemplo: Data: 01/01/2020,
Imprimir: 1 de janeiro de 2020.
Faça funções para retornar a data por extenso e utilize as
funções do 7º exercício para validar a entrada da data.
'''

from modulaData import validaData, validaEntrada

while True:
    data = input("Informe uma data no formato dd/mm/aaaa >> ")
    if validaEntrada(data) and validaData(data):
        break
    print("Data inválida!! Digite novamente...")

dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio',
         'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']
print(f"{dia} de {meses[mes-1]} de {ano}")
