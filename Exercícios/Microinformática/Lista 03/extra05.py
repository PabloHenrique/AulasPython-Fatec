#Ler três notas e fazer a média ponderada

n1 = float(input("Digite a nota do laboratório: "))
n2 = float(input("Digite a nota semestral: "))
n3 = float(input("Digite a nota do exame final: "))

mediaFinal = (n1*2 + n2*3 + n3*5) // (2+3+5)

print(f"Notas recebidas: {n1}, {n2} e {n3}")
print(f"O resultado da média é: {mediaFinal}")