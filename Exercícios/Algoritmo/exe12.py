#Ler dois valores inteiros e determinar o maior

v1 = int(input("Infome o primeiro valor: "))
v2 = int(input("Infome o segundo valor: "))

if v1 == v2:
    print("Os valores são iguas")
else:
    if v1 > v2:
        print(f"{v1} é o maior valor")
    else:
        print(f"{v2} é o maior valor")