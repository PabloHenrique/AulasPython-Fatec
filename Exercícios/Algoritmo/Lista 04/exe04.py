#Ler três valores inteiros e determinar o maior

v1 = int(input("Informe o primeiro valor: "))
v2 = int(input("Informe o segundo valor: "))
v3 = int(input("Informe o terceiro valor: "))

if v1 > v2 and v1 > v3:
    print(f"{v1} é o maior valor")
else:
    if v2 > v3:
        print(f"{v2} é o maior valor")
    else:
        print(f"{v3} é o maior valor")