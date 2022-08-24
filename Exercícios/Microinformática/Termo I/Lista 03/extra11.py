#Jogo Caça Níqueis
'''
O  programa  deverá  sortear  três  números  aleatórios  (1  a  99)  e  as  seguintes  regras  deverão  ser consideradas:
Se nenhumnúmero for igual, o apostador perde o jogo, se dois números forem iguais, o apostador ganhará 5 vezes o valor da aposta.
Se acertar os três ganhará 100 vezes o valor da aposta. Imprimir o valor ganho pelo apostador.
'''

from random import randint

valorA = float(input("Digite o valor da aposta: "))
print(f"Valor: R${valorA}")
print("\nSorteio!\n")

sortn1 = randint(1,99)
sortn2 = randint(1,99)
sortn3 = randint(1,99)

print(f"Número 1:{sortn1}")
print(f"Número 2:{sortn2}")
print(f"Número 3:{sortn3}\n")

if(sortn1 != sortn2 and sortn1 != sortn3):
    print("Nenhum ponto.\nNenhum número igual encontrado.\n\nFim de jogo!")

elif(sortn1 == sortn2 and sortn1 == sortn3):
    print("Parabénss!! Você acertou todos os números! (100x)")
    premio = valorA * 100
    print(f"Valor ganho: R${premio}")

else:
    print("Boaaa! Você acertou! (5x)")
    premio = valorA * 5
    print(f"Valor ganho: R${premio}")

