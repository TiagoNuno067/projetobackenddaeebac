lista = []
for i in range(1,6):
    usu = str(input('Nome:')).strip().capitalize()
    lista.append(usu)

lista.sort() 

print(lista)