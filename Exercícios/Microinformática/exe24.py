#Mostrar a sequência dos primeiros números de Fibonacci

num = 0
anterior = 0
proximo = 0

while(proximo < 100):
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    if(proximo == 0):
        proximo = proximo + 1
"""
while(cont <= 50):
    num = num - anterior
    anterior = num - anterior
    print(num, end=" ")
    cont+=1
"""