class Pessoa:
    def __init__(self, __nome, __idade):
        self.__nome = __nome
        self.__idade = __idade
    
    def falar(self):
        print("Oi")

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade

    def __str__(self):
        print("Meu nome é %s e tenho %d anos" % (self.__nome, self.__idade))

class Superheroi(Pessoa):
    def __init__(self, nome, idade, poder):
        super().__init__(nome, idade)
        self.poder = poder
    
    def utilizar_poder(self):
        print("Utilizei o poder %s!" % self.poder)
    
joao = Pessoa("João", 21)
joao.falar()
joao.__str__()
print(joao.get_nome())

heroi = Superheroi("Lucas", 34, "Raio")
heroi.falar()
heroi.utilizar_poder()