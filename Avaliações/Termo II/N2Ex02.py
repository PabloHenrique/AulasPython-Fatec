'''
Faça um programa em Python que leia dados de N contas bancárias
(número,  saldo).
Após a inserção, apresente um menu com as opções:
1.Listagem de número da contae saldo de todas inseridos
2.Saque: pedir o número da conta, fazer a busca e se encontrar, pedir o valor a ser retirado.

Altere o valor do saldo emitindo a mensagem, “Saque efetuado!!”.
Caso não encontre, exibir a mensagem “Conta não cadastrada”.
3.Encerrar
'''
import time

print("Iniciando operações.")
print("Digite as informações das contas bancárias.")
contas = {}

'''
    contas = {
        "numero": 250.000
    }
'''
def Listar():
    for n, t in contas.items():
        print(f'Número: {n} - Saldo: {t}')
    print()

while True:
    numero = int(input("\nDigite o número da conta: "))
    saldo = float(input("Digite o saldo: "))
    if numero not in contas:
        contas[numero] = saldo
    else:
        print("\n\nERRO! Conta já cadastrada.")
        time.sleep(1.5)

    print("-"*20)
    print("\nDeseja cadastrar outra conta? [S/N]")
    op = input("-> ")
    if op == 'N':
        break
    elif op != 'N' and op != 'S':
        print("ERRO! Opção não encontrada...")
        time.sleep(2)

print("Finalizado! Recebemos as suas informações.")
print("\nO que você gostaria: "
  "\n1. Listar os dados das contas"
  "\n2. Saque"
  "\n3. Encerrar")

op2 = int(input("-> "))
if op2 == 1:
    if contas:
        print("-"*20)
        Listar()
        print("-"*20)
    else:
        print("ERRO! Não foram encontradas contas.")

elif op2 == 2:
    while True:
        numConta = int(input("Informe o número da conta que deseja sacar: "))
        if numConta in contas:
            print("-"*20)
            print(f"\nSelecionado a conta de número: {numConta}"
                  f"\nSaldo disponível: {contas[numConta]}")
            print("-"*20)
            valorSaque = float(input("Informe o valor desejado: "))
            contas[numConta] -= valorSaque
            print("...")
            time.sleep(2)
            print("Saque efetuado!!")
            print(f"Novo saldo: {contas[numConta]}")
            break
        else:
            print("ERRO! Conta não cadastrada")

elif op2 == 3:
    print("\n\nFoi um prazer!")
    print("Obrigado por utilizar nosso sistema :D")

else:
    print("ERRO! Opção inválida.")

print(contas)