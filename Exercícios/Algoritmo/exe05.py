#Ler a distância de um percurso e a velocidade média de um veículo. Calcular tempo necessário para concluir o trajeto.

distancia = float(input("Informe a distância do percurso (km): "))
velocidade = float(input("Informe a velocidade média do veículo (km/h): "))

tempo = distancia/velocidade

print(f"O tempo total do percurso é {tempo} horas")