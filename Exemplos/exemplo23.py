#Listas com dicionários
brasil = []

estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}

estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}

brasil.append(estado1)
brasil.append(estado2)

print("-"*50)
print(estado1)
print(estado2)
print(brasil)

#Selecionando os dados
print("-"*50)

print(brasil[0]['uf'])
print(brasil[0]['sigla'])
print(brasil[1]['uf'])
print(brasil[1]['sigla'])