'''
5.	Fazer um programa em Python para verificar se uma determinada String é palíndromo.
Exs.: ANA - MUSSUM – OVO
'''
palavra = input('Entre com uma palavra >> ').upper()
print(palavra)
print(palavra[::-1])
if palavra == palavra[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')