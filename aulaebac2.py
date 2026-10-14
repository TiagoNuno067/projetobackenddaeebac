convidados_vip = ['Alice', 'Bob', 'Carol']
def verificar_idade(idade):
    if idade >= 18:
        return '"Entrada permitida. Bem-vindo ao evento!'
    else:
        return 'Entrada negada. Este evento é apenas para maiores de idade.'


def verificar_vip(nome):
    if nome in convidados_vip:
        return 'Você é um convidado VIP! Aproveite o evento com acesso especial'
    else:
        return 'Você não é convidado Vip'


idade = int(input('Digite sua idade:'))

if idade >= 18:
    convidados = verificar_idade(idade)
    print(convidados)

    nome = str(input('Digite seu nome:').strip().capitalize())
    vip = verificar_vip(nome)
    print(vip) 

else:
    print('Você é de menor não pode participar.')