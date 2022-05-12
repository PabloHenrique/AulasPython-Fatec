'''
9.Uma receita para produzir um bolo conta com 2 xicaras de farinha de trigo, 3 ovos e 5 colheres de leite
(estes dados são constantes nesta receita). Você deve escrever um programa em Python que  dados como entrada A
(quantidade de xicaras de farinha de trigo), B (quantidade de ovos) e C (quantidade de  colheres  de  leite)
todos  valores  inteiros,  o  programa  deve  mostrar  quantos  bolos  podem  ser produzidos.

Veja a simulação:
Ex.     1A =  4 B = 6 e  C = 10  produzirá a saída: 2 bolos.
Ex.     2A =  4 B = 6 e C = 9  produzirá a saída: 1 bolo.
Ex.     3A = 10 B = 10 e C = 25  produzirá a saída: 3 bolos.
'''

A = int(input('Informe a quantidade (de xícaras) de farinha de trigo: '))
B = int(input('Informe a quantidade de ovos: '))
C = int(input('Informe a quantidade (de colheres) de leite: '))

A = A//2
B = B//3
C = C//5

if A<B and A<C:
    print(f'{A} bolo(s)')
elif B<C:
    print(f'{B} bolo(s)')
else:
    print(f'{C} bolo(s)')
