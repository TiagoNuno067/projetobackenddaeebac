from datetime import date
ano = int(input('ano de nascimento:'))
idade = date.today().year - ano

if idade >= 16 and idade < 18:
    print(f'{idade} anos você ja pode votar')

elif idade >= 18:
    print(f'{idade} anos você ja pode tirar a habilitação.')

else:
    print(f'Você não tem idade nem para votar ou tirar a habilitação.')