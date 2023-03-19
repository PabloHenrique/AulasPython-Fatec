from time import sleep

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

class LSE:
    def __init__(self):
        self.Inicio = None

    def Ins_Inicio(self, val):
        p = No(val)
        p.setProx(self.Inicio)
        self.Inicio = p

    def Ins_Fim(self, val):
        p = No(val)
        if (self.Inicio==None): #listaVazia
            self.Inicio = p
        else:
            q = self.Inicio
            while (q.getProx() != None):#enquando o Q não for o último
                q = q.getProx()
            q.setProx(p)

    def ImprimirLista(self):
        p = self.Inicio
        print("\nInicio --> ", end='')
        while (p != None):
            print(p.getInfo(), "--> ", end='')
            p = p.getProx()
        print("None")

    def Rem_Inicio(self):
        self.Inicio = self.Inicio.getProx()

    def Rem_Meio(self, r):
        p = self.Inicio
        while (p.getProx() != r):
            p = p.getProx()

        p.setProx(r.getProx())

    def Rem_Fim(self):
        if (self.Inicio.getProx()==None): #Só tem um nó
            self.Inicio = None
        else:
            p = (self.Inicio)
            while(p.getProx()!= None): #Enquanto P não for o último
                q = p
                p = p.getProx()
            q.setProx(None)

    def Procurar(self, val):
        p = (self.Inicio)

        while (p != None and p.getInfo() != val):
            p = p.getProx()

        return p

    def Ins_Depois(self, r, val):
        p = No(val)
        p.setProx(r.getProx())
        r.setProx(p)

    def Ins_Antes(self, r, val):
        p = No(val)
        q = self.Inicio
        while q.getProx() != r:
            q = q.getProx
        p.setProx(r)
        q.setProx(p)

    def Ins_Ordenado(self, val):
        q = self.Inicio
        while (q != None) and (q.getInfo() <= val):
            q = q.getProx()
        if q == None:
            L.Ins_Fim(val)
        else:
            L.Ins_Antes(q, val)

L = LSE()  #Criando uma lista simplesmente encadeada
while True:
    print("-"*40)
    print("01 - Inserir no Inicio da lista")
    print("02 - Imprimir a lista")
    print("03 - Inserir no fim da lista")
    print("04 - Remover o primeiro número da lista")
    print("05 - Remover o último número")
    print("06 - Consultar valor da lista")
    print("07 - Remover um valor")
    print("08 - Inserir valor em depois de um valor")
    print("09 - Inserir valor em antes de um lugar")
    print("10 - Inserir valores de uma forma ordenada")#N1
    print("00 - Sair do programa")

    op = int(input("\nDigite a opção: "))

    if op == 0:
        print("Claro! Iremos encerrar o programa!")
        sleep(0.5)
        break

    elif op == 1:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Inicio(val)
        print("Feito com sucesso!")
        sleep(0.5)
        L.ImprimirLista()

    elif op == 2:
        if L.Inicio == None:
            print("Lista Vazia!")
            sleep(0.5)
        else:
            L.ImprimirLista()
            sleep(0.5)

    elif op == 3:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Fim(val)
        print("Feito com sucesso!")
        sleep(0.5)
        L.ImprimirLista()

    elif op == 4:
        if L.Inicio == None:
            print("Lista Vazia!")
            sleep(0.5)
        else:
            L.Rem_Inicio()
            sleep(0.5)
            print("Removido!")
            sleep(0.5)
            L.ImprimirLista()

    elif op == 5:
        if L.Inicio == None:
            print("Lista Vazia!")
            sleep(0.5)
        else:
            L.Rem_Fim()
            sleep(0.5)
            print("Removido!")
            sleep(0.5)
            L.ImprimirLista()

    elif op == 6:
        val = int(input("Digite o valor a procurar: "))
        r = L.Procurar(val)
        if (r == None):
            sleep(0.5)
            print("Valor não encontrado.")
            sleep(0.5)
            L.ImprimirLista()
        else:
            sleep(0.5)
            print("\nValor = ", r.getInfo())
            sleep(0.5)
            L.ImprimirLista()

    elif op == 7:
        val = int(input("Digite o valor a remover: "))
        r = L.Procurar(val)
        if (r == None):
            sleep(0.5)
            print("Valor não encontrado.")
            sleep(0.5)
            L.ImprimirLista()
        else:
            if (r == L.Inicio): #Se ele for o primeiro
                L.Rem_Inicio()
                sleep(0.5)
                print("Removido com sucesso! [INI]")
                sleep(0.5)
                L.ImprimirLista()
            else:
                if(r.getProx() == None): #Se ele for o último
                    L.Rem_Fim()
                    sleep(0.5)
                    print("Removido com sucesso! [FIM]")
                    sleep(0.5)
                    L.ImprimirLista()
                else:
                    L.Rem_Meio(r)
                    sleep(0.5)
                    print("Removido com sucesso!")
                    sleep(0.5)
                    L.ImprimirLista()

    elif op == 8:
        val = int(input("Digite o valor a procurar: "))
        r = L.Procurar(val)
        if (r == None):
            print("Valor não encontrado.")
            sleep(0.5)
            L.ImprimirLista()

        else:
            val = int(input("Digite o valor a inserir: "))
            if(r.getProx() == None): #É o último
                L.Ins_Fim(val)
                sleep(0.5)
                print("Removido com sucesso!")
                sleep(0.5)
                L.ImprimirLista()
            else:
                L.Ins_Depois(r, val)
                sleep(0.5)
                print("Feito com sucesso!")
                sleep(0.5)
                L.ImprimirLista()

    elif op == 9:
        val = int(input("Digite o valor a procurar: "))
        r = L.Procurar(val)
        if (r == None):
            print("Valor não encontrado.")
            sleep(0.5)
            L.ImprimirLista()
        else:
            val = int(input("Digite o valor a inserir: "))
            if (r == L.Inicio):  # É o primeiro
                L.Ins_Inicio(val)
                L.ImprimirLista()
            else:
                L.Ins_Antes(r, val)
                L.ImprimirLista()

    elif op == 10:
        val = int(input("Digite o valor a inserir: "))
        if L.Inicio == None: #vazia? insere inicio/fim (5)
            L.Ins_Inicio(val)
            L.ImprimirLista()
        else:
            if val < L.Inicio.getInfo():#está vazia? é menor que o primeiro nó? insere inicio (10)
                L.Ins_Inicio(val)
                L.ImprimirLista()
            else:
                L.Ins_Ordenado(val)
                L.ImprimirLista()

    else:
        print("Opaa, não encontramos uma opção válida!")
        sleep(0.5)