'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

'''
print('=' * 10)
print('Olá, bem vindo!')

while True:
    sair = False
    dec = input('\nVocê deseja executar o programa? [S/N]')
    if(dec == 'S'):
        print('=' * 10)
        print('Iniciando investigação...')
        entre = int(input('Informe quantas pessoas serão entrevistadas: '))
        pessoas = [0] * entre
        telefone = [0] * entre
        localCrime = [0] * entre
        moraVitima = [0] * entre
        deviaVitima = [0] * entre
        trabalhouVitima = [0] * entre
        ponto = [0] * entre

        for i in range(entre):
            print('-' * 10)
            print(f'\n\nEntrevistando >> Pesssoa {i+1}')
            pessoas[i] = input(f'Pessoa {i+1}: Qual é o seu nome? ')
            telefone[i] = input(f'Pessoa {i+1}: Você telefonou à vítima? ')
            localCrime[i] = input(f'Pessoa {i+1}: Esteve no local do crime? ')
            moraVitima[i] = input(f'Pessoa {i+1}: Você mora próximo ao local? ')
            deviaVitima[i] = input(f'Pessoa {i+1}: Há alguma dívida sua com a vítima? ')
            trabalhouVitima[i] = input(f'Pessoa {i+1}: Vocês trabalhavam juntos? ')
        print('\n---------- Fim das entrevistas ----------\n')
        print('Iniciando resultados!')
        for j in range(entre):
            if telefone[j] == 'S' and localCrime[j] == 'S' and moraVitima[j] == 'S' and deviaVitima[j] == 'S' and trabalhouVitima[j] == 'S':
                print(f'A {pessoas[j]} é ASSASSINA!')
    else:
        print('Até uma próxima!')
        break