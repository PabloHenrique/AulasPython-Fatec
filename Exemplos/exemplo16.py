#Exemplo do uso de Matriz
'''
Valor das posições = [0][0]
Sempre seguir: [linha][coluna]

0.0 _ 0.1 _ 0.2 _ 0.3 _ 0.4
1.0 _ 1.1 _ 1.2 _ 1.3 _ 1.4
2.0 _ 2.1 _ 2.2 _ 2.3 _ 2.4
3.0 _ 3.1 _ 3.2 _ 3.3 _ 3.4
4.0 _ 4.1 _ 4.2 _ 4.3 _ 4.5

'''
print("-" * 25)
print("Exemplo 01")
for i in range(5):
    for j in range(5):
        print(f'{i,j}', end=' ')
    print()

print("-" * 25)
print("Exemplo 02")
M = [[1,2,3],[4,5,6]]
for k in range(2):
    for l in range(3):
        print(f'{M[k][l]:02}', end=' ')
    print()

print("-" * 25)
print("Exemplo 03")
OM = [0] * 3

print('\nDigite os valores da Matriz: \n')
for m in range(3):
    OM[m] = [0] * 4
    for n in range(4):
        OM[m][n] = int(input(f'[Linha: {m+1}] e [Coluna: {n+1}] > '))
        #OM[m][n] = randint(1,20)

print('\nResultado da Matriz: \n')
for m in range(3):
    for n in range(4):
        print(f'{OM[m][n]:2}', end=' ')
    print()