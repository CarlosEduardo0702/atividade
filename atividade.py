class Pessoa:
    def __init__(self,nome,peso,idade,comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade

        self.estado = "parado"

    def parar(self):
        self.estado="parado"
    def comer(self,alimento):
        if self.estado=="parado":
            self.estado="comendo"
            print(f"{self.nome}está comendo{alimento}")
        elif self.estado=="comendo":
            print(f"{self.nome}já está comendo")
        else:
            print(f"{self.nome}não pode comer")
    def andar(self):
        if self.estado=="parado":
            self.estado="andando"
            print(f"{self.nome}está andando")
        elif self.estado=="andando":
            print(self.nome,"já está andando")
        else:
            print(f"{self.nome}não pode andar agora")
    def falar(self):
        if self.estado=="parado":
            self.estado="falando"
            print(f"{self.nome} está falando")
        elif self.estado=="falando":
            print(self.nome,"já está falando")
        else:
            print(f"{self.nome} não pode falar agora")
