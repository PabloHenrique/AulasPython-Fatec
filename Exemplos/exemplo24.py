estado = dict()
brasil = list()

print(" ------- Cadastrar ------- ")
quantidade = int(input("Informe a quantidade de informações: "))
print("\n")
for c in range(quantidade):
    estado['uf'] = input(f"Unidade Federativa {c+1}: ")
    estado['sigla'] = input(f"Sigla do Estado {c+1}: ")
    brasil.append(estado.copy())

#Apresentado os dados
print("="*40)

print(brasil)

print("="*40)
for estado in brasil:
    print(estado)

print("=" * 40)

for estado in brasil:
    for k, v in estado.items():
        print(F"O campo {k} tem valor {v}")

print("=" * 40)

for estado in brasil:
    for v in estado.values():
        print(F"{v}", end=' ')
    print()