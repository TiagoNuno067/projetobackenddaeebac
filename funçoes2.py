pessoas = ["Tiago", "Ariane", "Caio"]

def verificaridade(idade):
    if idade >= 18:
        print('Entrada permitida. Bem-vindo ao evento!')
        usu = str(input('Digite seu nome:')).strip()
        if usu in pessoas:
             print(f'Você é um convidado VIP! Aproveite o evento com acesso especial. Bem vindo {usu}!')
        else:
             print(f'Vc não é convidado!')
    else:
        print('Entrada negada. Este evento é apenas para maiores de idade.')

verificaridade(int(input('Digite sua idade:')))