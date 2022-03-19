#Exemplo - While - Para reiniciar um programa
#Verifica se um número é par ou ímpar, o usuário decide quando parar

resp = 'S'
while resp == 'S':
    print('~' * 40)
    num = int(input("Informe um número >> "))
    if num % 2 == 0:
        print('PAR')
    else:
        print('ÍMPAR')
    print('~'*40)
    resp = input("Deseja testar outro número? [S/N] >> ").upper()[0]