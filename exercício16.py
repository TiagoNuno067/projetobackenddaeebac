numeros = []

for c in range(1, 20):
    n = int(input('Digite um numero:'))
    numeros.append(n)
    menor = min(numeros) 
    maior = max(numeros) 

print(numeros) 
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')