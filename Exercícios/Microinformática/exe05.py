'''
5. Escreva um programa que armazene um valor de entrada em uma variável A e outro em uma
variável B. A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos
fazendo com que o valor que está em A passe para B e vice-versa. Ao final escrever os valores que
ficaram armazenados nas variáveis.
'''

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

#Desempacotamento de dados
#a,b = b,a

#Variável auxiliar
c = a
a = b
b = c

print(f"{a} e {b}")