dia = int(input('Digite o dia de seu nascimento:'))
mes = int(input('Digite o mês de seu nascimento:'))

if dia >= 21 and mes == 3 or mes == 4 and dia <= 19:
    print('Você é de Áries.')

elif mes == 4 and dia >= 20 or mes == 5 and dia <= 20:
    print('Você é de Touro.')

elif mes == 5 and dia >= 21 or mes == 6 and dia <= 20:
    print('Você é de gêmeos.')

elif mes == 6 and dia >= 21 or mes == 7 and dia <= 22:
    print('Você é de cancêr.')

elif mes == 7 and dia >= 23 or mes == 8 and dia <= 22:
    print('Você é de leão.')

elif mes == 8 and dia >= 23 or mes == 9 and dia <= 22:
    print('Você é de virgem.')

elif mes == 9 and dia >= 23 or mes == 10 and dia <= 22:
    print('Você é de libra.')

elif mes == 10 and dia >= 23 or mes == 11 and dia <= 21:
    print('Você é de escorpião.')

elif mes == 11 and dia >= 22 or mes == 12 and dia <= 21:
    print('Você é de sagitario.')

elif mes == 12 and dia >= 22 or mes == 1 and dia <= 19:
    print('Você é de capricórnio.')

elif mes == 1 and dia >= 20 or mes == 2 and dia <= 18:
    print('Você é de aquario.')

elif mes == 2 and dia >= 19 or mes == 3 and dia <= 20:
    print('Você é de peixes.') 

else:
    print('Data invalida.')