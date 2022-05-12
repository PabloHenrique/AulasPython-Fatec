'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''

distPercorrida = float(input("Informe a quantidade de km percorridos com o carro: "))
diasAlugado = int(input("Informe a quantidades de dias alugados: "))

carroDia = 60
kmRodado = 0.15

despesa = carroDia * diasAlugado + kmRodado * distPercorrida

print(f"O preço total a pagar pelo carro alugado é: R${despesa:.2f}")