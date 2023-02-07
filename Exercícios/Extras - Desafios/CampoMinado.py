'''Desafio Campo Minado'''

Campo = []
from random import randint
for i in range(5):
    L = []
    for j in range(5):
        L.append(0)
    Campo.append(L)

#Criação do campo
def ApresentarCampo():
    txt = " 1  2  3  4  5 "
    txt = txt.center(22)
    print(txt)
    for i in range(5):
        print(i+1," ", end="")
        for j in range(5):
            print(F" {Campo[i][j]} ", end="")
        print()

posX = []
posY = []

def SortearBombas():
    for i in range(5):
        posX.append(randint(1,5))
        posY.append(randint(1,5))

ApresentarCampo()

#Sorteando as bombas
SortearBombas()
for i in range(5):
    for j in range(5):
        Campo[posX[i]][posY[j]].append("X")

ApresentarCampo()
