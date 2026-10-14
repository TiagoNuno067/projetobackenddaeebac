cod = int(input('Digite o código:')) 

if cod == 1:
    print('Alimento não perecível.')

elif cod == 2 or cod == 3 or cod == 4:
    print('Alimento perecível')

elif cod == 5 or cod == 6:
    print('Vestuário')

elif cod >= 8 and cod <= 15:
    print('Limpeza e utensílios domésticos')

else:
    print('Código Inválido.')