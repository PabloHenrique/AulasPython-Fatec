class No:
    def __init__(self, val):
        self.info = val
        self.prox = None
    def getInfo(self):
        return self.info
    def getProx(self):
        return self.prox
    def setInfo(self, val):
        self.info = val
    def setProx(self, proximo):
        self.prox = proximo

'''
p = No(30)
q = No(50)
r = No(60)
s = No(70)

p.setProx(q)
q.setProx(r)
r.setProx(s)

while (p!=None):
    print(p.getInfo(), "--> ", end='')
    p = p.getProx()
print("None")
'''


class LSE:
    def __init__(self):
        self.Inicio = None

    def Ins_Inicio(self, val):
        p = No(val)
        p.setProx(self.Inicio)
        self.Inicio = p

    def Ins_Fim(self, val):
        p = No(val)
        p.setProx(self.Inicio)
        self.Inicio = p

    def ImprimirLista(self):
        p = self.Inicio
        print("\nInicio --> ", end='')
        while (p!=None):
            print(p.getInfo(),"--> ", end='')
            p = p.getProx()
        print("None")

L = LSE() #Criando uma lista simplesmente encadeada
while True:
    print("\n1 - Inserir no Inicio da lista")
    print("2 - Imprimir a lista")
    print("3 - Inserir no fim da lista")
    print("0 - Sair do programa")

    op = int(input("\nDigite a opção: "))

    if op == 0:
        print("Claro! Iremos encerrar o programa!")
        break

    if op == 1:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Inicio(val)

    if op == 2:
        if L.Ins_Inicio == None:
            print("Lista Vazia!")
        else:
            L.ImprimirLista()

    if op == 3:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Inicio(val)

