'''4. Escreva um programa em Python que contenha uma função que retorne True caso o
argumento passado seja primo e False caso contrário. O argumento será sempre um valor inteiro.
Peça um número, chame o método e imprima se o mesmo é número primo ou não.'''

def numPrimo(num):
  if num >= 1:
      for i in range(2, num):
        if num % i != 0:
            return True
        else:
            return False
            break

print("Digite o número: ")
numero = int(input("--> "))

res = numPrimo(numero)

if (res == True):
  print("É primo!")
elif(res == False):
  print("Não é primo!")
else:
  print("Não entendi")

