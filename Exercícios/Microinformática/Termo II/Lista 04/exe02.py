'''
Faça uma lista de tamanho 50 preenchido com o seguinte valor: (i+5∗i)%(i+1), sendo i a posição do
elemento na lista. Em seguida imprima a lista na tela.
'''
L = []
for i in range(50):
    L.append((i+5*i)%(i+1))
print(*L)