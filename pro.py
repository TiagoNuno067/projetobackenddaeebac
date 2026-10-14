n = int(input())

strn = str(n) 

if strn == strn[::-1]:
    print(f'É um palíndromo {strn}')
else:
    print(f'Não é um palindromo {strn}')