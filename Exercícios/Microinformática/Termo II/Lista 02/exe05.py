'''5. Faça um programa em Python que imprima todos os números primos de um intervalo
informado pelo usuário. Utilize o método do exercício 4 para verificar se o número é primo ou não.'''

def numPrimo(num):
  if num >= 1:
      for i in range(2, num):
        if num % i != 0:
            return True
        else:
            return False
            break

print("Digite o intervalo: ")
ini = int(input("Inicio --> "))
fim = int(input("Fim --> "))

for num in range(ini, fim+1):
  if numPrimo(num):
    print(F"{num} ", end=" ")

