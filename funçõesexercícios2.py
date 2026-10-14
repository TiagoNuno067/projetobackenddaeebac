def maiornumero(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

lista = [2,9,4,5]

maior = maiornumero(lista)
print(maior)