a = int(input('Primero numero:'))
b = int(input('Segundo numero:')) 

while b != 0:
    a, b = b, a % b

print(f'O máximo divisor comum é {a}')
