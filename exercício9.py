from math import sqrt
numero = int(input('Digite um numero:'))

raiz_quadrada = sqrt(numero)

c = 0
while c <= raiz_quadrada:
    c += 1

print(f'A raiz quadrada de {numero} é {raiz_quadrada}')
print(f'O numero que mais se aproxima da raiz é {c - 1}')