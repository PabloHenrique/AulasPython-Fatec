'''
Faça um programa em Python para verificar se um CPF, digitado pelo usuário, está correto ou não.
Para isto considere uma string de 11 caracteres para armazenar sem pontos ou traço, apenas
números (Faça a validação para a entrada ser apenas composta de números).
A verificação do CPF está em calcular os dois dígitos de controle e comparar com os digitados, se os
dois calculados forem iguais aos dois digitados, o CPF digitado é válido, caso contrário, o CPF é
inválido.
Cálculo do 1º dígito: Soma os 9 primeiros números do CPF multiplicados de 1 a 9 e calcula-se o
resto desta soma por 11. Se o resto for igual a 10, então o dígito é 0.
Cálculo do 2º dígito: Soma os 9 primeiros números do CPF multiplicados de 9 a 1 e calcula-se o
resto desta soma por 11. Se o resto for igual a 10, então o dígito é 0.
Após o cálculo, compara-se com as respectivas posições da string e informe se o CPF é válido ou
inválido
'''

cpf = input('Informe o CPF (com 11 dígitos) >> ')
s1 = 0
s2 = 0
for i in range(9):
    s1 += int(cpf[i]) * (i+1)
    s2 += int(cpf[i]) * (9-i)
d1 = s1 % 11
if d1 == 10:
    d1 = 0
d2 = s2 % 11
if d2 == 10:
    d2 = 0
if d1 == int(cpf[9]) and d2 == int(cpf[10]):
    print('CPF válido!!')
else:
    print('CPF inválido!!')

