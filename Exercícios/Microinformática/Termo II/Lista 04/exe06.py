'''
João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem
certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos números
abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o
valor.
'''

def contaLeds(numero):
    leds = 0
    L = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    for d in str(numero):
        leds += L[int(d)]
    return leds

N = int(input())
for i in range(N):
    V = int(input())
    print(contaLeds(V),'leds')
