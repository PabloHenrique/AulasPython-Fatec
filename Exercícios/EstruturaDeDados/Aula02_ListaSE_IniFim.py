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
        self.Inicio = None #Controlador
        self.Fim = None #Controlador

    def Ins_Inicio(self, val):
        p = No(val)
        if self.Inicio == None: #A lista está vazia?
            self.Fim = p
        else:
            p.setProx(self.Inicio)

        self.Inicio = p #Volta o inicio para o P

    def Ins_Fim(self, val):
        p = No(val)
        if self.Inicio == None: #A lista está vazia?
            self.Inicio = p
        else:
            self.Fim.setProx(p)

        self.Fim = p #Volta o inicio para o P

    def Imprime(self):
        p = self.Inicio
        print("\nInicio --> ", end='')
        while (p != None):
            print(p.getInfo(), "--> ", end='')
            p = p.getProx()
        print("None")

    def Rem_Inicio(self):
        if(self.Inicio == self.Fim):
            self.Inicio = None
            self.Fim = None
        self.Inicio = self.Inicio.getProx()

    def Rem_Fim(self):
        if self.Inicio.getProx()==None: #Se tiver somente 1 nó
            self.Inicio = None
            self.Fim = None
        else:
            p = self.Inicio
            while (p.getProx() != self.Fim):
                p = p.getProx()
            p.setProx(None)
            self.Fim = p

    def Trans_Ini_Fim(self):
        p = self.Inicio #Coloca o P no Inicio (controlador)
        self.Inicio = self.Inicio.getProx() #Novo primeiro vai ser o próximo de P
        p.setProx(None) #Próximo de P vai ser None
        self.Fim.setProx(p) #Proximo do fim é o P
        self.Fim = p #fim é o P

    def Trans_Fim_Ini(self):
        p = self.Inicio #Coloca o P no Inicio
        while (p.getProx() != self.Fim): #Enquanto o P não for o penúltimo
            p = p.getProx()
        p.setProx(None)
        self.Fim.setProx(self.Inicio)
        self.Inicio = self.Fim # O Fim vai para o Inicio
        self.Fim = p

L = LSE()

while True:
    print("-"*40)
    print("1 - Inserir no inicio da lista")
    print("2 - Imprimir a lista")
    print("3 - Inserir no fim da lista")
    print("4 - Remover o inicio da lista")
    print("5 - Remover o fim da lista")
    print("6 - Transferir o Inicio para o Fim")
    print("7 - Transferir o Fim para o Inicio")

    op = int(input("\nDigite a opção: "))

    if op == 0:
        print("Programa finalizado!")
        sleep(0.5)
        break

    elif op == 1:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Inicio(val)
        sleep(0.5)
        print("Feito com sucesso!")


    elif op == 2:
        if L.Inicio == None:
            print("Lista Vazia!")
            sleep(0.5)
        else:
            L.Imprime()
            sleep(0.5)

    elif op == 3:
        val = int(input("Digite o valor a inserir: "))
        L.Ins_Fim(val)
        sleep(0.5)
        print("Feito com sucesso!")
        L.Imprime()

    elif op == 4:
        if L.Inicio == None:
            print("\nLista vazia!")
        else:
            L.Rem_Inicio()
            sleep(0.5)
            print("Feito com sucesso!")
            L.Imprime()

    elif op == 5:
        if L.Inicio == None:
            print("\nLista vazia!")
        else:
            L.Rem_Fim()
            sleep(0.5)
            print("Removido com sucesso!")
            L.Imprime()

    elif op == 6:
        if L.Inicio == None:
            print("\nLista vazia!")
        else:
            if L.Inicio == L.Fim: #Só tem um nó
                print("Já é o último!")
            else:
                L.Trans_Ini_Fim()
                sleep(0.5)
                print("Tranferido com sucesso!")
                L.Imprime()

    elif op == 7:
        if L.Inicio == None:
            print("\nLista vazia!")
        else:
            if L.Inicio == L.Fim: #Só tem um nó
                print("Já é o último!")
            else:
                L.Trans_Fim_Ini()
                sleep(0.5)
                print("Tranferido com sucesso!")
                L.Imprime()

    else:
        print("Opção não encontrada :9 ")
        print("Programa finalizado!")
        sleep(0.5)
        break