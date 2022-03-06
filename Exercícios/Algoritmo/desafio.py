#Informar o próximo segundo
#sendo que o próximo segundo de 60 é 1

s = int(input("Informe um segundo: "))

prox_s = (s+1)%60

print(f"O próximo segundo é: {prox_s}")