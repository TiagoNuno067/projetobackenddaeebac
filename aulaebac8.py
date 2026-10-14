# definindo uma classe
class animal:
    #construtor
    def __init__(self, nome):
        self.nome = nome
    #método
    def comer(self):
        print(f'O {self.nome} está comendo.')
        
#herdando uma classe
class cachorro(animal):
    def latir(self):
        print(f'O {self.nome} esta a latir')

meu_cachorro = cachorro('Goku')
meu_cachorro.comer() 
meu_cachorro.latir()
