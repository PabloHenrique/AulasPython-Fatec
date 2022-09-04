'''1.Escreva um programa em Python que contenha uma função que
peça um número e verifique se ele é par ou ímpar.
No principal, chame a função.'''

def parOuImpar(num):
  if num%2==0:
    return True
  else:
    return False

print("Digite o número: ")
num = int(input(''))

parOuImpar(num)
if parOuImpar == True:
  print("É par!")
else:
  print("É ímpar!")