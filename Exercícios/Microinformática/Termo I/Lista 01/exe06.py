'''
6. Implemente um programa para ler o salário mensal atual de um funcionário e o percentual de
reajuste. Calcular e escrever o valor do novo salário.
'''

salario =  float(input("Informe o sálario do funcionário: "))
reajuste = float(input("Informe o reajuste do funcionário: "))

novoSalario = salario + (salario * reajuste/100)

print(f"O novo salário do funcionário é {novoSalario}")