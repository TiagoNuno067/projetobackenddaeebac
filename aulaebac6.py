array = [1,2,3,4,5,6,7,7,8,9,10]
dici = {}
for i in array:
    if i not in dici:
        dici[i] = 1
    else:
        dici[i] += 1
        
for chave, valor in dici.items():
    if chave == valor:
        print(chave)