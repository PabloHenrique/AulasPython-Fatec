#Input das variáveis
n1 = int(input("\nDigite o primeiro número: "))
n2 = int(input("Digite o segundo: "))

#Const do número 2
num2 = n2

#Declarar variáveis da estrutura de repetição
uni1 = 0
uni2 = 0
termina = 0
inv = 0
ult = 0

#Code - Validação
if(n1 == 0 or n2 == 0):
    print("\nErro, números inválidos")
else:
    print("\nAnalisando o número ...\n")
    while True:
        #Selecionar a unidade.
        uni1 = n1 % 10
        uni2 = n2 % 10
        #Verificar se o resto das unidades são iguais.
        if(uni1 == uni2):
            while(n2 > 0):
                #Inverter os valores
                ult = n2 % 10
                inv = (inv * 10) + ult
                # Guardar a unidade na var Termina e somar com o número solicitado
                termina = (termina * 10) + inv
                n2 = n2 // 10

                #Inverter resultado
                resultado = int(str(inv)[::-1])
        else:
            break
    #Se termina existir, mostrar.
    if(termina):
        print(f"{n1} termina com {resultado}")
    else:
        print(f"{n1} NÃO termina com {num2}")