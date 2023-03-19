class Pessoa:
    #self: separa o que pertence a classe ou não
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print("Nome: ", self.nome)
        print("Idade ", self.idade)

    def aniversario(self):
        self.idade += 1

x = Pessoa("Pablo", 17)
print("-"*10)
x.mostrar()
x.aniversario()
x.mostrar()
print("-"*10)

y = Pessoa("Henrique", 18)
y.mostrar()
y.aniversario()
y.mostrar()
print("-"*10)