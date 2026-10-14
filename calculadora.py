print('SOMA [1] SUBTRÇÃO [2] MULTIPLICAÇÃO [3] DIVISÃO[4] POTENCIA[5]')

a = int(input('Escolha uma opção:'))

if a == 1:
    print('VOCÊ ESCOLHEU SOMA:')
    n1 = int(input('digite um numero:'))
    n2 = int(input('digite um numero:'))
    soma = n1 + n2
    print(soma)

if a == 2:
    print('VOCÊ ESCOLHEU SUBTRAÇÃO:')
    n1 = int(input('Digite um numero'))
    n2 = int(input('digite um numero:'))
    subtração = n1 - n2
    print(subtração)

if a == 3:
    print('VOCÊ ESCOLHEU MULTIPLICAÇÃO:')
    n1 = int(input('Digite um numero'))
    n2 = int(input('digite um numero:'))
    mult = n1 * n2
    print(mult)

if a == 4:
    print('VOCÊ ESCOLHEU DIVISÃO:')
    n1 = int(input('Digite um numero:'))
    n2 = int(input('Digite um numero:'))
    divisao = n1 / n2
    print(divisao)

if a == 5:
    print('VOCÊ ESCOLHEU POTÊNCIA:')
    n1 = int(input('Digite um numero:'))
    n2 = int(input('Digite um numero:'))
    potencia = n1 ** n2
    print(potencia)
