pessoas = {
    'nome': 'Pablo',
    'sexo': 'M',
    'idade': '18'
}

print("-"*50)

print(pessoas.items())
print(F'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print("-"*50)

del pessoas['sexo']
pessoas['altura'] = 190
for k, v in pessoas.items():
    print(F"{k} = {v}")

