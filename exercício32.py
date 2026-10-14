limite = 20
a, b = int(input('Digite um numero')), int(input('Digite um numero:'))

while a <= limite:
    a, b = b, a + b
    print(a, end= ' ') 
