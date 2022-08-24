#Jogo de apostas
from random import randint

valorAposta = float(input("Digite o valor da aposta: R$"))
numApostado = int(input("Número entre 1 e 36: "))

if (numApostado < 1 or numApostado > 36):
    print("Número inválido.")
else:
    numSorteado = randint(1,36)
    print(f"Número sorteado >> {numSorteado}")
    if numSorteado == numApostado:
        print(f"Acertou o número, ganhou R${valorAposta * 5:.2f}")
    elif (numSorteado-1)//12 == (numApostado-1)//12:
        print(f"Acertou a dúzia, ganhou R${valorAposta * 3:.2f}")
    elif numSorteado%2 == numApostado%2:
        print(f"Acertou a paridade, ganhou R${valorAposta * 2:.2f}")
    else:
        print("Perdeu a aposta.")