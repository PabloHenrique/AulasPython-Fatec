#Ler 2 valores inteiros e calcular a soma entre eles
'''
10.Faça um programa para ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2  valores  lidos
(incluindo  os  valores  lidos  na  soma). O  programa  deve  validar  que  o  1º valor informado seja menor que o
2º valor. O programa deve permitir que o usuário possa executá-lo novamente.
'''

v1 = 0

while True:
    print('=' * 50)
    v1 = int(input("Informe o 1° valor: "))
    v2 = 1
    soma = 0

    while v2 < v1:
        v2 = int(input("Informe o 2° valor: "))
        contador = v1 + 1
        while v2 > contador:
            soma += contador
            contador += 1

    print(f'Soma entre {v2} e {v1} = {soma}')
    print('=' * 25)
    continua = input("Deseja realizar mais uma soma? [Sim] [Não]\n")
    if continua[0] == 'N' or continua[0] == 'n':
        break

