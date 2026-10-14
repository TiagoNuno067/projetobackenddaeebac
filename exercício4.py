sexo = str(input('Sexo: M/F')).strip().upper()
altura = float(input('Altura:'))

if sexo == 'M':
    pesom = (72.7 * altura) - 58
    print(f'Você é homem seu peso ideal é {pesom}')

elif sexo == 'F':
    pesof = (62.1 * altura) - 44.7
    print(f'Você é mulher seu peso ideal é {pesof}')

else:
    print('Erro: dados invalidos:')