#Ler dois números e selecionar a opção desejada

num1 = int(input("\n\nDigite o primeiro número: "))
num2 = int(input("Digite o outro número: "))
print("\n\nOpções: \n+ (Adição)\n- (Subtração)\n* (Multiplicação)\n/ (Divisão)\n\n")
oper = input("Digite a operação desejada: ")

if(oper == '+'):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif(oper == '-'):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif(oper == '*'):
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif(oper == '/'):
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
