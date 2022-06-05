print('='*20)
print('Iniciando o programa!')

print("\n\nDigite os valores desejados")
print("OBS: Caso digite 0, o programa será encerrado.")

M = []
cont = 0
while True:
    num = int(input('>>> '))
    cont = cont + 1
    if(num == 0):
        break
    else:
        if(len(M) == 0 or num > M[len(M)-1]):
            M.append(num)
        for i in range(cont):
            if (num < M[i]):
                M.insert(i, num)
print("\n\nResultado: ")

print({ *M })