'''Jogo da Velha'''

import time
from random import randint

def showBoard(board):
    print("-" * 12)
    print("  1  2  3")
    for i in range(3):
        print(i+1, end="")
        for j in range(3):
            print(F"|{board[i][j]}|", end='')
        print()
    print("-" * 12)

def CheckBoard(board, playerOnePoint, playerTwoPoint):


    if playerOnePoint >= 1:
        return print(F"Ohooho, temos um vencedor! Ponto para o jogador: {playerOne}")
    elif playerTwoPoint >=1:
        return print(F"Ohooho, temos um vencedor! Ponto para o jogador: {playerTwo}")

playerOne = input("Digite o nome do jogador 1: ")
playerTwo = input("Agora, o nome do jogador 2: ")

print(f"Bem vindos: {playerOne}, {playerTwo}!")
playerOnePoint = 0
playerTwoPoint = 0

while True:
    print("\nDeseja iniciar um novo jogo? [Sim/Não]")
    op = input("-> ")
    if op == "Sim" or op == "SIM" or op == "sim" or op == "S":
        time.sleep(1)
        board = [[" " for i in range(3)] for j in range(3)]
        showBoard(board)
        jogadas = 0
        print("\nJogador 1 será o X")
        print("Jogador 2 será o O")
        win = 1
        while win == 1:
            print(f"{playerOne}, escolha as posições de 1 a 3")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            board[linha-1][coluna-1] ="X"
            showBoard(board)
            jogadas += 1
            #---
            print(f"{playerTwo}, escolha as posições de 1 a 3")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            board[linha - 1][coluna - 1] = "0"
            showBoard(board)
            jogadas += 1
            # JOGADOR 1 - VERTICAL
            vencedorOne = False
            vencedorTwo = False
            if jogadas >= 3:
                if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
                    vencedorOne = True
                    playerOnePoint += 1
                    break
                if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
                    vencedorOne = True
                    playerOnePoint += 1
                    break
                if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
                    vencedorOne = True
                    playerOnePoint += 1
                    break
                # JOGADOR 1 - HORIZONTAL
                if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
                    vencedorOne = True
                    playerOnePoint += 1
                    break
                if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
                    vencedorOne = True
                    playerOnePoint += 1
                    break
                if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
                    vencedorOne = True
                    playerOnePoint += 1
                    break
                # JOGADOR 1 - DIAGONAL
                if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                    vencedorOne = True
                    playerOnePoint += 1
                    break
                if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
                    vencedorOne = True
                    playerOnePoint += 1
                    break
                # ------------------------------------------------------------------
                # JOGADOR 2 - VERTICAL
                if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
                    vencedorTwo = True
                    playerTwoPoint += 1
                    break
                if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
                    vencedorTwo = True
                    playerTwoPoint += 1
                    break
                if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
                    vencedorTwo = True
                    playerTwoPoint += 1
                    break
                # JOGADOR 2 - HORIZONTAL
                if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
                    vencedorTwo = True
                    playerTwoPoint += 1
                    break
                if board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
                    vencedorTwo = True
                    playerTwoPoint += 1
                    break
                if board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
                    vencedorTwo = True
                    playerTwoPoint += 1
                    break
                # JOGADOR 2 - DIAGONAL
                if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                    vencedorTwo = True
                    playerTwoPoint += 1
                    break
                if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
                    vencedorTwo = True
                    playerTwoPoint += 1
                    break
            if vencedorOne == True:
                print("Opaaa! Temos um vencedor!")
                print(F"Ponto para o jogador: {playerOne}")
                win = 2
            elif vencedorTwo == True:
                print("Opaaa! Temos um vencedor!")
                print(F"Ponto para o jogador: {playerTwo}")
                win = 2

    elif op == "Não" or op == "Nao" or op == "NAO" or op == "NÃO" or op == "N":
        print("Encerrando...")
        time.sleep(1)
        break
    else:
        print("Não entendi...")
        print("Tente uma opção válida!")

print("Foi um prazer! ")