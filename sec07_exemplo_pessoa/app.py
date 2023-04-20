class Pessoa:
    def falar(self):
        print("Oi!")

class Arthur(Pessoa):
    def falar(self):
        print("Oi, meu nome é Arthur")

class Matheus(Pessoa):
    pass

arthur = Arthur()
arthur.falar()

matheus = Matheus()
matheus.falar()