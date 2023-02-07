print("\n\nPablo Henrique Vieira De Nadai")
print("Trabalho Algoritmo 02 - Insert sort\n\n")
print('='*20)
print('Iniciando o programa!')

print("\nDigite os valores desejados")
print("OBS: Caso digite 0, o programa será encerrado.")

#Vetor utilizado
M = []
cont = 0
#Laço infinito até atender a condição
#Solicitará números para o vetor
while True:
    num = int(input('>>> '))
    # 0 para encerrar o programa
    if (num == 0):
        break
    else:
        cont = cont + 1
        if (len(M) == 0 or num > M[len(M)-1]):
            M.append(num)
        for i in range(cont):
            if (num < M[i]):
                M.insert(i, num)
print("\n\nResultado: ")

print({ *M })