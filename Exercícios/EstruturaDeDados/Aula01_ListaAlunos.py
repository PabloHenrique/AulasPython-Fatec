def inserir_fim(A, n, nota1, nota2):
    A.append([n, [nota1, nota2]])

def inserir_inicio(A, n, nota1, nota2):
    A.insert(0,[n, [nota1, nota2]])

def inserir_desejada(A, des, n, nota1, nota2):
    A.insert(des, [n, [nota1, nota2]])

def imprimir(A):
    for i in range (len(A)):
        print("\nNome: ",A[i][0])
        print("Nota 1: ", A[i][1][0])
        print("Nota 2: ", A[i][1][1])

def mostrar_media(A):
    for i in range (len(A)):
        med = (A[i][1][0] + A[i][1][1] )/2
        print("Nome: ",A[i][0], "Media Final: ", med)

def buscar_aluno(A, nome):
    for i in range(len(A)):
       if A[i][0] == nome:
           return i
    return -1

L = []
while True:
    print("-"*45)
    print("\n1 - Inserir alunos no fim da lista"
          "\n2 - Mostrar os alunos da lista"
          "\n3 - Mostrar o nome com a media final"
          "\n4 - Inserir alunos no inicio da lista"
          "\n5 - Consultar aluno"
          "\n6 - Remover aluno"
          "\n7 - Inserir alunos na posição X da lista"
          "\n8 - Inserir de forma ordenada"
          "\n9 - Organizar a lista"
          "\n0 - Sair do programa")
    print("-" * 45)
    op = int(input("Digite a opção:"))

    if op==0:
        break
    elif op==1:
        nome = input("Digite o nome do aluno:")
        n1 = float(input("Digite a nota 1:"))
        n2 = float(input("Digite a nota 2:"))
        inserir_fim(L, nome, n1, n2)

    elif op==2:
        print("\nListagem dos alunos:")
        imprimir(L)

    elif op==3:
        print("\nListagem  com a Media Final")
        mostrar_media(L)

    elif op == 4:
        nome = input("Digite o nome do aluno:")
        n1 = float(input("Digite a nota 1:"))
        n2 = float(input("Digite a nota 2:"))
        inserir_inicio(L, nome, n1, n2)

    elif op == 5:
        busca = input("Digite o aluno a ser buscado: ")
        pos = buscar_aluno(L, busca)
        if pos == -1:
            print("Aluno não existe")
        else:
            print("Dados do aluno:\n"
                  f"Posição: {pos}\n", L[pos])

    elif op == 6:
        busca = input("Digite o nome do aluno para remover: ")
        if buscar_aluno(L, busca) != -1:
            L.pop(buscar_aluno(L, busca))
            print("Excluído com sucesso!\n")
        else:
            print("Aluno não encontrado.")

    elif op == 7:
        busca = input("Digite o nome do aluno para localizar a posição: ")
        pos = buscar_aluno(L, busca)
        print(pos)
        if pos != -1:
            nome = input("Digite o nome do aluno para inserir: ")
            n1 = float(input("Digite a nota 1:"))
            n2 = float(input("Digite a nota 2:"))
            inserir_desejada(L, pos, nome, n1, n2)
        else:
            print("Nome não encontrado!")