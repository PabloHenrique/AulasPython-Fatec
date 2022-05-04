#Ler o salário fixo de um funcionário e calcular o salário final conforme a comissão.

salario = float(input("Informe o salário do funcionário: "))
vendas = float(input("Informe o valor total das vendas do funcionário: "))

comissao = vendas * 0.04
salario_final = salario + comissao

print(f"Salário fixo: R${salario:.2f}")
print(f"Comissão: R${comissao:.2f}")
print(f"Salário total: R${salario_final:.2f}")