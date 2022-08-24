#Ler número inteiro e verificar se é par ou ímpar

n = int(input("Informe um número: "))

if n < 0:
    n = n * -1
if n%2 == 0:
    print("Par!")
else:
    print("Ímpar!")