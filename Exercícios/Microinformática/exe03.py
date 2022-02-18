'''
3. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
'''

valor = float(input("Digite o valor em metros: "))
#1m = 100cm = 1,00cm
#1cm = 10mm = 1,0mm
cm = valor * 100
mm = cm * 10
print(f"O valor {valor} em mm é: {mm}")