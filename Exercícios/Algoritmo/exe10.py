#Ler tempo em segundos, calcular o equivalente em horas, minutos e segundos

tempo = int(input("Informe os segundos: "))

h = tempo//3600
m = (tempo%3600)//60
s = (tempo%3600)%60

print(f"{tempo} segundos é equivalente a: {h} horas, {m} minutos e {s} segundos")