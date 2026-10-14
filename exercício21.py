import datetime

dia = int(input('Digite o dia:'))
mes = int(input('Digite o mês:')) 
ano = int(input('Digite o ano:'))

anoatual = datetime.date.today().year
diaatual = datetime.date.today().day
mesatual = datetime.date.today().month

idade = anoatual - ano

if mes >= mesatual or dia >= diaatual:
    print(f' vc tem {idade - 1} anos de idade')


else:
    print(f'Vc tem {idade} anos de idade')