dia = int(input('Digite o dia:'))
mes = int(input('Digite o mês:'))
ano = int(input('Digite o ano:'))

if dia > 30 or dia > 31:
    print('Data invalida: o mês não possui esse dia')

elif mes > 12 or mes < 1:
    print('Data invalida: esse mês não existe.')

else:
    print(f'{dia}/{mes}/{ano}')