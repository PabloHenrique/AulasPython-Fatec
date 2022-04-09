#12. Bits Trocados
'''
As Ilhas Weblands formam um reino independente nos mares do Pacífico. Como é um reino recente,
a sociedade é muito influenciada pela informática. A moeda oficial é o Bit; existem notas de B$ 50,00,
B$10,00, B$5,00 e B$1,00. Você foi contratado(a) para ajudar na programação dos caixas automáticos
de um grande banco das Ilhas Weblands.

Tarefa
Os caixas eletrônicos das Ilhas Weblands operam com todos os tipos de notas disponíveis, mantendo
um estoque de cédulas para cada valor (B$ 50,00, B$10,00, B$5,00 e B$1,00). Os clientes do banco
utilizam os caixas eletrônicos para efetuar retiradas de um certo número inteiro de Bits.
Sua tarefa é escrever um programa que, dado o valor de Bits desejado pelo cliente, determine o
número de cada uma das notas necessário para totalizar esse valor, de modo a minimizar a
quantidade de cédulas entregues. Por exemplo, se o cliente deseja retirar B$50,00, basta entregar
uma única nota de cinquenta Bits. Se o cliente deseja retirar B$72,00, é necessário entregar uma
nota de B$50,00, duas de B$10,00 e duas de B$1,00.
'''
cinquenta = 0
dez = 0
cinco = 0
um = 0
bits = int(input("Quantidade de Bits desejado >> "))

cinquenta = bits//50
if cinquenta > 0:
    resto = bits%50
    print(f"{cinquenta} nota(s) de B$50,00")
else:
    resto = bits

dez = resto//10
if dez > 0:
    resto = resto%10
    print(f"{dez} nota(s) de B$10,00")

cinco = resto//5
if cinco > 0:
    resto = resto%5
    print(f"{cinco} nota(s) de B$5,00")

um = resto//1
if um > 0:
    print(f"{um} nota(s) de B$1,00")