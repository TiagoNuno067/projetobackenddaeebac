lista_de_produtos = []
dici = {}

def menu():
    return '''
    [1] Adicionar Produto 
    [2] Listar Produtos 
    [3] Remover Produto
    [4] Atualizar Produto
    [5] Sair'''


def main():
    while True:
        opção = menu()
        print(opção)
        usu = int(input('Gerenciar estoque:'))

        if usu == 5:
            break

        elif usu == 1:
            nomep = str(input('Nome do produto:')).strip() 
            nomeq = int(input('Quantidade do produto:'))
            nomepr = float(input('Preço do produto:'))
 
            lista_de_produtos.append(nomep)
            lista_de_produtos.append(nomeq) 
            lista_de_produtos.append(nomepr)

            for i in lista_de_produtos:

                if i not in dici:
                    dici[i] = 1
                else:
                    dici[i] += 1

        elif usu == 2:
            lista_de_produtos.sort(key= lambda x: (isinstance(x, str), x))
            for i in lista_de_produtos:
                print(i)

        elif usu == 3:
            usur = str(input('qual produto gostaria de remover:')).strip()
            for i in lista_de_produtos:
                if usur == i:
                    

main()