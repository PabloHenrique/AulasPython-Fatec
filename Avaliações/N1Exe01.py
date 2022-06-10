#Ler quantidade de estoque e calcular a média.

print("Digite >>>")
quantAtual = int(input("A quantidade atual de estoque: "))
quantMax = int(input("A quantidade máxima do estoque: "))
quantMin = int(input("A quantidade mínima do estoque: "))

quantMedia = ((quantMax + quantMin) / 2)

if (quantAtual >= quantMedia):
    print('Não efetuar compra')
else:
    print('Efetuar compra')