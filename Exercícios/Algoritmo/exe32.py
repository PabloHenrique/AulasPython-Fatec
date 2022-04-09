# Ler 10 números e soma-los

soma = 0
for i in range (1,11):
    n = float(input(f"Informe o {i} número: "))
    soma += n

print(f"\nA soma dos números é {soma}")