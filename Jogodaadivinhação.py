# importando o random
import random

# escrevendo na tela
print('Adivinhar um numero de 1 a 10')

while True:

    # validando o numero
    
    try:
        jogador = int(input('Digite um numero de 1 a 10:'))
        computador = random.randint(1, 10)
        
        if jogador == computador:
            break
        
        else:
            print('ERROU: tente outra vez.')

    except ValueError:
        print('Valor invalido:')


print('Parabens! você adivinhou.')
print('FIM DE JOGO')