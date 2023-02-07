''' Agenda telefônica usando dicionários '''

import time
agenda = {}
'''
    agenda = {
        "nome": ["000", "111", "222"]
    }
'''
def criarMenu():
    return input('1. Incluir Nome\n'
                 '2. Incluir Telefone\n'
                 '3. Excluir Nome\n'
                 '4. Excluir Telefone\n'
                 '5. Consultar Telefones\n'
                 '6. Listar Telefones\n'
                 '7. Sair\n\n'
                 'Digite a opção -> '
                 )

def apresentarMenu(texto):
    print("="*50)
    print(texto.center(50))
    print("="*50)

def incluirNovoNome():
    nome = input("Digite o nome -> ")
    print()
    if nome not in agenda:
        incluirTelefone(nome)
    else:
        print('Erro! Nome já cadastrado.\n')
        time.sleep(1)
        print("...\n")
        time.sleep(1)

def incluirTelefone(nome):
    contato = []
    print(f"Inserindo telefones para: {nome}")
    while True:
        numeros = input("Digite um telefone ou 0 para sair -> ")
        if numeros == '0':
            break
        if numeros in contato:
            print('Erro! Número já cadastrado.\n')
            time.sleep(1)
            print("...\n")
            time.sleep(1)
        else:
            contato.append(numeros)
    agenda[nome] = contato

def excluirTelefone(nome, telefone):
    agenda[nome].remove(telefone)

def excluirNome(nome):
    agenda.pop(nome, 'Erro! O contato não consta na agenda.')

def consultarTelefone(nome):
    print(nome, end=':')
    for telefone in agenda[nome]:
        print(f' {telefone}', end='')
    print()

def listarTelefone():
    for contato in agenda.keys():
        consultarTelefone(contato)
        print()


while True:
    print("=" * 50)
    print('Agenda On-line')
    print("=" * 50)
    opcao = criarMenu()
    match opcao:
        case '1':
            apresentarMenu('Incluir novo Nome')
            incluirNovoNome()

        case '2':
            apresentarMenu('Incluir novo Telefone')
            nomeTelefone = input("Digite o nome do contato que você deseja incluir o telefone: ")
            incluirTelefone(nomeTelefone)

        case '3':
            apresentarMenu('Excluir Nome')
            nome = input("Digite o nome do contato que deseja excluir\n-> ")
            print()
            excluirNome(nome)

        case '4':
            apresentarMenu('Excluir Telefone')
            nome = input("Digite o nome do contato em que o numero está\n-> ")
            telefone = input("Digite o telefone que deseja excluir\n-> ")
            excluirTelefone(nome, telefone)

        case '5':
            apresentarMenu('Consultar Telefones')
            nome = input("Digite o nome do contato em que o numero está\n-> ")
            consultarTelefone(nome)

        case '6':
            apresentarMenu('Listar Telefones')
            listarTelefone()

        case '7':
            break

        case _:
            print("Erro! Opção não encontrada.")
