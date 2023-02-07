#Dicionários

'''
Com os dicionários, podemos armazenar os dados a partir de indices personalizados.

Tuplas = ()
Listas = []
Dicionários = {}

'''

dados = {'nome': 'Pablo',
         'idade': '18',
         'sexo': 'M',
         'contato': '(14)99XXX-XXXX',
         'e-mail': 'pablo@email.com'
         }

del dados['sexo']

print(dados["nome"])
print(dados["idade"])
#print(dados['sexo'])

print("-"*80)

print("Retornar todos os valores do dicionário: ")
print(dados.values())

print("\nRetornar todos os índices: ")
print(dados.keys())

print("\nRetornar o dicionário completo: ")
print(dados.items())

print("-"*80)
print("\n")
for keys, values in dados.items():
    print(F"{keys.upper()}: {values}")