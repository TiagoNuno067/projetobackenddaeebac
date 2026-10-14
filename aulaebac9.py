class modpokemon: 
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def mostrar_nome(self):
        print(f'O nome do pokemon é {self.nome}')

    def mostrar_peso(self):
        print(f'O peso do pokemon é Kg{self.peso}')

picachu = modpokemon('Pikachu', 67.45)

picachu.mostrar_nome()
picachu.mostrar_peso()