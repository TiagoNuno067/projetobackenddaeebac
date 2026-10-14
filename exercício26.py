import datetime

ano_de_nascimento = int(input('Digite o ano de nascimento:')) 

anoatual = datetime.date.today().year

idade = anoatual - ano_de_nascimento

if idade < 16:
    print(f'Você tem {idade} anos. Não votante')

elif idade >= 18 and idade <= 65:
    print(f'Você tem {idade} anos. Eleitor obrigatório.')

elif idade >= 16 and idade <= 18 or idade > 65:
    print(f'Você tem {idade} anos. Eleitor facultativo')