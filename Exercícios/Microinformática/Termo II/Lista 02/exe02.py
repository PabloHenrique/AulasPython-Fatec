'''2. Escreva um programa em Python que implemente uma função potência, que receba uma
base e um expoente por parâmetro e retorne o valor da base elevada ao expoente. O expoente é
sempre maior ou igual a zero, e os números são sempre inteiros. Peça uma base e um expoente,
chame a função e imprima o resultado.'''

def potencia (base, expo):
  pot = 1
  for i in range(expo):
    pot = pot * base
  return pot

print("Digite os números desejados!")
print("Informe a base: ")
base = int(input("--> "))
print("Informe o expoente: ")
exp = int(input("-->"))

r = potencia(base, exp)
print(r)