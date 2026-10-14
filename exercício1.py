from math import sqrt
print("CALCULO DE EQUAÇÃO DE SEGUNDO GRAU:")

coeficientes = {"a": int(input('Valor de a:')), "b": int(input('Valor de b:')), "c": int(input('Valor de c:'))}

delta = (coeficientes["b"] ** 2) - 4 * coeficientes["a"] * coeficientes["c"]


x1 = (coeficientes["b"] + sqrt(delta)) / (2 * coeficientes["a"])
x2 = (coeficientes["b"] - sqrt(delta)) / (2 * coeficientes["a"])

print(delta)

if x1 > 0 and x2 > 0:
    print('Raizes reais:')
else:
    print('Raizes negativas: sem solução.')
    
print(f'conjunto solução: {x1}, {x2}')