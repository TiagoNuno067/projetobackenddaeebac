array = [1,3,4,5,5,6,7,6,5] 

dici = {}

for i in array:
    if i not in dici:
        dici[i] = 1

    else:
        dici[i] += 1

for chave, valor in dici.items():
    if valor == 1:
        print(chave)