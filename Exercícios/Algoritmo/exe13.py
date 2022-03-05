#Ler velocidade máxima de uma rodovia e a velocidade de um carro. Verificar o motorista sofrerá multa ou não.

velMax = float(input("Digite a velocidade máxima permitida(km/h): "))
velCarro = float(input("Digite a velocidade do veículo(km/h): "))

if(velCarro > velMax):
    print("Você foi multado. Ultrapassou a velocidade permitida!")
else:
    print("Boaa, tudo certo com a sua velocidade!")