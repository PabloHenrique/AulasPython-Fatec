from time import sleep


class No:
    def __init__(self, val):
        self.esq = None
        self.info = val
        self.dir = None

    def getEsquerda(self):
        return self.esq

    def getDireita(self):
        return self.dir

    def getInfo(self):
        return self.info

    def setEsquerda(self, x):
        self.esq = x

    def setDireita(self, x):
        self.dir = x

    def setInfo(self, x):
        self.info = x

class LDE:
    def __init__(self):
        self.Inicio = None
        self.Fim = None

    def Ins_Inicio(self, val):
        p = No(val)
        p.setDireita(self.Inicio)
        if self.Inicio == None:
            self.Fim = p
        else:
            self.Inicio.setEsquerda(p)
        self.Inicio = p

    def Ins_Fim(self, val):
        p = No(val)
        p.setEsquerda(self.Inicio)
        if self.Inicio == None:
            self.Inicio = p
        else:
            self.Fim.setDireita(p)

        self.Fim = p

    def Rem_Inicio(self):
        if L.Inicio == L.Fim: #Somente um nó
            self.Inicio = None
            self.Fim = None
        else:
            self.Inicio = self.Inicio.getDireita()#O Inicio passa para o próximo
            self.Inicio.setEsquerda(None)

    def Rem_Fim(self):
        if L.Fim == L.Inicio: #Somente um nó
            self.Inicio = None
            self.Fim = None
        else:
            self.Fim = self.Fim.getEsquerda()  # O Fim passa para antepenultimo
            self.Fim.setDireita(None)

    def Consultar(self, val):
        p = self.Inicio
        while (p != None and p.getInfo() != val):
            p = p.getDireita()
        return p

    def Rem_Meio(self, r):
        p = r.getEsquerda()
        q = r.getDireita()
        p.setDireita(q)
        q.setEsquerda(p)

        #r.getEsquerda.setDireita(r.getDireita)
        #r.getDireita.setEsquerda(r.getEsquerda)

    def Imprime(self):
        p = self.Inicio
        print("\nInicio --> ", end='')
        while (p != None):
            print("<--", p.getInfo(), "--> ", end='')
            p = p.getDireita()
        print("None\n")

L = LDE()

while True:
    print("-" * 40)
    print("1 - Inserir no Inicio da lista")
    print("2 - Inserir no Fim da lista")
    print("3 - Imprimir")
    print("4 - Remover no Inicio")
    print("5 - Remover no Fim")
    print("6 - Consultar um valor")
    print("7 - Remover um valor")
    print("0 - Encerrar o programa")

    op = int(input("\nDigite a opção: "))

    if op == 0:
        print("Programa finalizado!")
        break

    elif op == 1:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Inicio(val)
        print("Feito com sucesso!")

    elif op == 2:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Fim(val)
        print("Feito com sucesso!")

    elif op == 3:
        if L.Inicio == None:
            print("Lista Vazia!")
        else:
            L.Imprime()


    elif op == 4:
        if L.Inicio == None:  # Está vázia?
            print("\nLista vazia!")
        else:
            L.Rem_Inicio()
            print("Removido com sucesso!")
            L.Imprime()

    elif op == 5:
        if L.Inicio == None:  # Está vázia?
            print("\nLista vazia!")
        else:
            L.Rem_Fim()
            print("Removido com sucesso!")
            L.Imprime()

    elif op == 6:
        val = int(input("Digite o valor a procurar: "))
        r = L.Consultar(val)
        if r == None:
            print("Não existe na lista 🤔")
        else:
            print("Valor encontrado = ", r.getInfo())

    elif op == 7:
        val = int(input("Digite o valor a remover: "))
        r = L.Consultar(val)
        if r == None:
            print("Não existe na lista 🤔")
        else:
            if r == L.Inicio: # É o primeiro?
                L.Rem_Inicio()
                print("Removido com sucesso INI!")
                L.Imprime()
            else:
                if r == L.Fim:  # É o último?
                    L.Rem_Fim()
                    print("Removido com sucesso FIM!")
                    L.Imprime()
                else:
                    L.Rem_Meio(r)
                    print("Removido com sucesso!")
                    L.Imprime()