def decorator(func):
    def wrepper():
        print('Primeiro passo:') 
        func() 
        print('Segundo passo:')

    return wrepper

@decorator 

def falar():
    print('Oi eu sou o Tiago')

falar()