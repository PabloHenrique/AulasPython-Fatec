'''3. Faça um programa em Python que implemente uma função INVERTE que receba um
número como parâmetro e retorne este número escrito ao contrário. Ex: 4312 → 2134. Peça um
número, chame a função e imprima o resultado.'''

def reverseString(num):
    return num[::-1]

print("Digite o número: ")
num = input("--> ")
str(num)
r = reverseString(num)

print(r)