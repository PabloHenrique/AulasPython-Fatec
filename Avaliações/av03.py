# Cauê Vicentini Ruiz - Henrique Queiroz de Paula - Tiago Gili Lopes
# Ánalise e Desenvolvimento de Sistemas noite
# Programação em microinformática - Avaliação - 30/03/2022
'''
Exercício TABUADA:

Escreva um programa que gere a tabuada de 1 até um valor n>0 na forma de uma tabela tal que, na posição  da  linha i
e  coluna j da  tabela,  deve-se  encontrar  o  valor i*j.'''

n = int(input('Informe um número para a geração da tabuada: '))

for i in range(1, n+1):
    for j in range(i, (n*i)+1, i):
        print(f'{j:2}', end=' ')
    print()