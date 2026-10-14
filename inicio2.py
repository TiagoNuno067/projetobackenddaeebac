lista = [1,2,3,3,3,3,4,4,5,5]

dici = {}

for i in lista:
    if i not in dici:
        dici[i] = 1
    else:
        dici[i] += 1

soma = 0
for chave, valor in dici.items():
    if valor == 1:
        soma += chave

print(soma)