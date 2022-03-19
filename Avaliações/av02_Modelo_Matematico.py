# Cauê Vicentini Ruiz - Henrique Queiroz de Paula - Pablo Henrique Vieira de Nadai - Tiago Gili Lopes
# Ánalise e Desenvolvimento de Sistemas noite
# Programação em microinformática - Avaliação - 16/03/2022
# Exercício Vai 1: ver a quantidade de operações vai 1 que resultam da adição de 2 números

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

u1 = n1%10
d1 = n1%100//10
c1 = n1//100

u2 = n2%10
d2 = n2%100//10
c2 = n2//100

vai1 = 0
vai1 = ((u1+u2)//10) + ((d1+d2+((u1+u2)//10))//10) + ((c1+c2+((d1+d2)//10))//10)

print(f'{vai1} "vai 1"')