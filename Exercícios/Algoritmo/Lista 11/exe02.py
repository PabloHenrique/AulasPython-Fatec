from random import randint

RESP = ['c', 'b', 'a', 'd', 'a', 'b', 'c', 'd', 'e', 'b']
ALT = []
ponto = 0
aluno = 0
while True:
    cont = input("Deseja ler a nota de um aluno? [S/N]")
    if (cont == 'S'):
        aluno += 1
        print('Digite suas notas: ')
        for j in range(10):
            ALT.append(input(f'Questão {j+1}: '))
            if ALT[j] == RESP[j]:
                ponto += 1
        print(f"Nota do aluno 0{aluno}: {ponto}")
    else:
        print('FIM')
        break