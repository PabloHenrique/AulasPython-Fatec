#Ler 1 número e calcular o seu fatorial
'''
12. Elabore um programa que calcule N! (fatorial de N), sendo que o valor inteiro de N é fornecido
pelo usuário.
'''

fatorial = 1
n = int(input("Informe um número: "))

for i in range (n):
    fatorial *= i+1

print(fatorial)
