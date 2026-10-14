def meu_decorator(func):
    def wrapper():
        print('ola') 
        func() 
        print('Mundo') 

    return wrapper

@meu_decorator

def des():
    print('Ola viado')

des() 