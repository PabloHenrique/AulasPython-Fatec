'''
7. Implemente um programa para ler o preço do litro do combustível de um carro, ler o desempenho
do veículo (km/l) e a distância entre duas cidades (km), e informar quantos litros, e quanto dinheiro
vai ser gasto para fazer uma viagem entre as duas cidades.
'''

precoLitro = float(input("Informe o preço do litro do combustivél: "))
desempenho = float(input("Informe o desempenho(km/l) do veículo: "))
distancia = float(input("Informe a distância entre as cidades desejadas: "))

totalcombustivel = distancia / desempenho
precoTotal = totalcombustivel * precoLitro

print(f"O total gasto de combustivél será de {totalcombustivel} e o preço total que será gasto é {precoTotal}")