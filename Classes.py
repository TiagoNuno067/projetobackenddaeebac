# ==========================================
# 1. DEFINIÇÃO DA CLASSE MÃE (ANIMAL)
# ==========================================
class Animal:
    # O método __init__ é o construtor. Ele inicializa os atributos do objeto.
    def __init__(self, nome, idade):
        self.nome = nome      # Armazena o nome do animal
        self.idade = idade    # Armazena a idade do animal

    # Método genérico que será herdado pelas classes filhas
    def emitir_som(self):
        mensagem = "O animal emitiu um som genérico."
        print(mensagem)
        return mensagem       # Boa prática para compatibilidade com testes automatizados


# ==========================================
# 2. DEFINIÇÃO DAS CLASSES FILHAS (SUBCLASSES)
# ==========================================

# A classe Cachorro herda tudo da classe Animal através de (Animal)
class Cachorro(Animal):
    
    # Sobrescrita do método emitir_som específico para o Cachorro
    def emitir_som(self):
        mensagem = "O cachorro latiu!"
        print(mensagem)
        return mensagem


# A classe Gato também herda tudo da classe Animal
class Gato(Animal):
    
    # Sobrescrita do método emitir_som específico para o Gato
    def emitir_som(self):
        mensagem = "O gato miou!"
        print(mensagem)
        return mensagem


# ==========================================
# 3. PROGRAMA PRINCIPAL (MAIN)
# ==========================================
def main():
    # Instanciação (criação) de um objeto da classe Cachorro
    # Passamos o nome "Rex" e a idade 5 para o construtor herdado de Animal
    meu_cachorro = Cachorro("Rex", 5)
    
    # Instanciação (criação) de um objeto da classe Gato
    # Passamos o nome "Mia" e a idade 3 para o construtor herdado de Animal
    meu_gato = Gato("Mia", 3)
    
    # Chamada dos métodos de forma polimórfica:
    # Mesmo tendo o mesmo nome, cada objeto responde com o seu comportamento específico
    print(f"Dados do Cão -> Nome: {meu_cachorro.nome}, Idade: {meu_cachorro.idade}")
    meu_cachorro.emitir_som()  # Deve exibir: "O cachorro latiu!"
    
    print() # Linha em branco para organização visual
    
    print(f"Dados do Gato -> Nome: {meu_gato.nome}, Idade: {meu_gato.idade}")
    meu_gato.emitir_som()      # Deve exibir: "O gato miou!"


# Garante que o programa principal roda quando executamos o ficheiro diretamente
if __name__ == "__main__":
    main()