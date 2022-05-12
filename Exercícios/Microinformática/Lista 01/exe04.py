'''
4. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
o total em segundos.
'''

dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

horas = horas + (dias * 24)
minutos = minutos + (horas * 60)
segundos = segundos + (minutos * 60)

print(f"O total de segundos será {segundos}")