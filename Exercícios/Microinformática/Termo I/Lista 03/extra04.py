#Ler o salário e a prestação de um trabalhador

salario = float(input("Informe o valor do salário do trabalhador: "))
prestacao = float(input("Informe o valor da prestação: "))

if prestacao <= (salario * 0.2):
    print("Empréstimo concedido!")
else:
    print("Empréstimo não concedido!")