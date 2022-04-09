#Ler 1 número e mostrar seus divisores

n = int(input("Informe um número: "))

for i in range (1,(n//2)+1):
    if n%i == 0:
        print(f"{i}", end=" ")
print(f"e {n}")