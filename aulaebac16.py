def mdc(a, b):
    while b != 0:
        a, b = b, a % b

    return a

num1 = int(input('Digite um numero:'))
num2 = int(input('Digite um numero:'))

maximo_divisor_comum = mdc(num1,num2)

print(f'O maximo divisor comum é {maximo_divisor_comum}')

