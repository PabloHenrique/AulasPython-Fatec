#Adição e remoção de elementos
#Busca
#Acesso

sequencial = []

class No:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.Inicio = None
        self._Tamanho = 0

    def append(self, val):
        if self.Inicio:
            pointer = self.Inicio
            while (pointer.next): #enquando o pointer tiver um next (diferente de None)
                pointer = pointer.next
            pointer.next = No(val)
        else:
            self.Inicio = No(val) #armazenar o nó no Inicio
        self._Tamanho += 1

    def __len__(self):
        #Retorna o tamanho da lista
        return self._Tamanho

    def _getnode(self, index):
        pointer = self.Inicio
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Index out of range 😐")
        return pointer

    def set(self, index):
        # lista.set(1, 10)
        pass

    def __getitem__(self, index):
        #Recuperar o valor do elemento
        #a = lista[6]
        pointer = self._getnode(index)
        if pointer:
            return pointer.info
        else:
            raise IndexError("Index out of range 😐")

    def __setitem__(self, index, val):
        #lista[2] = 6
        pointer = self._getnode(index)
        if pointer:
            pointer.info = val
        else:
            raise IndexError("Index out of range 😐")

    def index(self, val):
        i = 0
        pointer = self.Inicio
        while pointer:
            if pointer.info == val:
                return i
            pointer = pointer.next
            i+=1
        raise ValueError(f"{val} Isn't there in the list 😐")

    def insert(self, index, val):
        no = No(val)
        if index == 0:
            no.next = self.Inicio
            self.Inicio = no
        else:
            pointer = self._getnode(index-1)
            no.next = pointer.next
            pointer.next = no
        self._Tamanho += 1

    def ImprimirLista(self):
        pointer = self.Inicio
        print("\nInicio --> ", end='')
        while pointer:
            print(pointer.info, "--> ", end='')
            pointer = pointer.next
        print("None")

L = LinkedList()

while True:
    print("-"*50)
    print("Escolha uma opção: ")
    print("1. Inserir um elemento no final da lista"
          "\n2. Trocar um valor em x posição"
          "\n3. Verificar valor na posição da lista"
          "\n4. Pesquisar o tamanho"
          "\n5. Inserir valor em x posição")
    op = int(input("--> "))
    match op:
        case 1:
            val = int(input("Digite o valor: "))
            L.append(val)
            print("Sucesso!")
            L.ImprimirLista()

        case 2:
            val = int(input("Digite o valor: "))
            print("OBS: Lembre-se, index = 0!")
            pos = int(input("Seria em qual posição?"))
            L.__setitem__(pos, val)
            print("Sucesso!")
            L.ImprimirLista()

        case 3:
            val = int(input("Digite o valor: "))
            print(F"Valor encontrado na posição: {L.index(val)}")
            L.ImprimirLista()

        case 4:
            L.ImprimirLista()
            print(F"Claro! A sua lista tem: {len(L)} posições")

        case 5:
            val = int(input("Digite o valor: "))
            print("OBS: Lembre-se, index = 0!")
            pos = int(input("Seria em qual posição?"))
            L.insert(pos, val)
            print("Sucesso!")
            L.ImprimirLista()

        case _:
            print("Opção não encontrada")
            sair = input("Deseja encerrar? Sim/Não\n")
            sair.upper()
            if sair == "SIM":
                exit()
            else:
                print("Perfeito!")
                pass
