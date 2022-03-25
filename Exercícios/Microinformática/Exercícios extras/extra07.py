#Ler a distância e a quantidade de litros gastos. Verificar um percurso e o consumo
'''
Menor que 8km/l - Venda o carro
Entre 8 e 14km/l  - Econômico
Maior que 14km/l - Supereconômico
'''

dist = float(input("Digite a distância do percurso: [Km]"))
quantL = float(input("Digite a quantidade de litros gastos: [L]"))

consumo = dist / quantL

print("Situação do veículo:\n")
if (consumo < 8):
    print("Venda o carro!")
elif(consumo < 14):
    print("Econômico")
else:
    print("Super econômico")