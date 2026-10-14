soma = lambda num1, num2: num1 + num2
sub = lambda num1, num2: num1 - num2
mult = lambda num1, num2: num1 * num2
div = lambda num1, num2: num1 / num2
pot = lambda num1, num2: num1 ** num2

def menu():

    operadores = ["Soma", "Subtração", "Multiplicação", "Divisão", "Potencição"]
    opções = [f'{i + 1} - {operadores[i]}' for i in range(5)]

    print('--- MENU DE OPERADORES ---')
    for item in opções:
        print(item)

def main():

    menu()
    while True:
        try:
            usu = int(input('(0 para sair) Escolha um dos operadores:'))

            while usu < 0 or usu > 5:
                print('Escolha uma das opções disponíveis.')
                usu = int(input('Escolha um dos operadores'))

            if usu == 1:

                try:
                    num1 = int(input('Numero:'))
                    num2 = int(input('Numero:'))
                    print(f'A soma é {soma(num1,num2)}')

                except ValueError:
                    print('entrada invalida: precisam ser numeros.')

            elif usu == 2:
                try:
                    num1 = int(input('Numero:'))
                    num2 = int(input('Numero:'))
                    print(f'O resultado da subtração é {sub(num1,num2)}')

                except ValueError:
                    print('entrada invalida: precisam ser numeros.')

            elif usu == 3:
                try:
                    num1 = int(input('Numero:'))
                    num2 = int(input('Numero:'))
                    print(f'O resultado da multiplicação é {mult(num1,num2)}')
                except ValueError:
                    print('entrada invalida: precisam ser numeros.')

            elif usu == 4:
                try:
                    num1 = int(input('Numero:'))
                    num2 = int(input('Numero:'))
                    print(f'O resultado da divisão {div(num1,num2)}')

                except ValueError:
                    print('entrada invalida: precisam ser numeros.')

                except ZeroDivisionError:
                    print('Não existe divisão por zero.')

            elif usu == 5:
                try:
                    num1 = int(input('Numero:'))
                    num2 = int(input('Numero:'))
                    print(f'O resultado da potência é {pot(num1,num2)}')

                except ValueError:
                    print('entrada invalida: precisam ser numeros.')

            elif usu == 0:
                break

        except ValueError:
            print('Dados invalidos')
            
    print('--- FIM DO PROGRAMA ---')

main()