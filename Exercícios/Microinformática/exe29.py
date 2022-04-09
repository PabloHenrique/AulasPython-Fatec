#Lê 1 número e verifica se é um quadrado perfeito
'''
14.Uma forma de verificar se um número é um quadrado perfeito é calculando a soma dos números
ímpares, veja:

1  quadrado perfeito
1 + 3 = 4  quadrado perfeito
1 + 3 + 5 = 9  quadrado perfeito
1 + 3 + 5 + 7 = 16  quadrado perfeito
1 + 3 + 5 + 7 + 9 = 25  quadrado perfeito
1 + 3 + 5 + 7 + 9 + 11 = 36  quadrado perfeito
E assim por diante...

Elabore um programa que leia um número inteiro e verifique se ele é ou não quadrado
perfeito.
'''
impares = 1
quad = 0
perfeito = False

n = int(input("Informe um número: "))
while quad < n:
    quad += impares
    impares += 2
    if quad == n:
        perfeito = True
        break;
if perfeito:
    print(f"{n}  quadrado perfeito")
else:
    print("Não quadrado perfeito")