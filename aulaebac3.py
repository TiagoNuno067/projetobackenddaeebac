array = [2,3,9,6]

maior = array[0]
menor = array[0]

for i in array:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
    
print(array)
print(f'O maior valor é {maior} e o menor é {menor}')
print(f'A soma entre eles é {maior + menor}')