# Dicionário global para armazenar o stock
estoque = {}

def adicionar_produto():
    print("\n--- Adicionar Produto ---")
    nome = input("Nome do produto: ").strip()
    
    if nome in estoque:
        print("Erro: Este produto já existe! Use a opção de atualizar a quantidade.")
        return

    # Validação da quantidade
    while True:
        try:
            quantidade = int(input(f"Quantidade de '{nome}': "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Erro: Insira um número inteiro válido para a quantidade.")

    # Validação do preço
    while True:
        try:
            preco = float(input(f"Preço de '{nome}': "))
            if preco < 0:
                print("O preço não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Erro: Insira um número decimal válido para o preço.")

    # Adiciona ao dicionário com a estrutura pedida
    estoque[nome] = {
        "quantidade": quantidade,
        "preco": preco
    }
    print(f"Produto '{nome}' adicionado com sucesso!")


def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if not estoque:
        print("O estoque está vazio.")
        return

    # Ordena o dicionário em ordem alfabética pelas chaves (nome do produto) usando lambda
    produtos_ordenados = sorted(estoque.items(), key=lambda item: item[0].lower())

    for nome, dados in produtos_ordenados:
        print(f"{nome}: {dados['quantidade']} - {dados['preco']:.2f}€")


def remover_produto():
    print("\n--- Remover Produto ---")
    nome = input("Nome do produto a remover: ").strip()

    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print("Erro: Produto não encontrado no estoque.")


def atualizar_quantidade():
    print("\n--- Atualizar Quantidade de Produto ---")
    nome = input("Nome do produto: ").strip()

    if nome not in estoque:
        print("Erro: Produto não encontrado no estoque.")
        return

    while True:
        try:
            nova_qtd = int(input(f"Nova quantidade para '{nome}': "))
            if nova_qtd < 0:
                print("A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Erro: Insira um número inteiro válido.")

    estoque[nome]["quantidade"] = nova_qtd
    print(f"Quantidade de '{nome}' atualizada para {nova_qtd} com sucesso!")


def exibir_menu():
    print("\n================ MENU ================")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Remover produto")
    print("4. Atualizar quantidade de produto")
    print("5. Sair")
    print("======================================")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            atualizar_quantidade()
        elif opcao == "5":
            print("A terminar o programa... Até breve!")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 5.")

# Executa o programa principal
if __name__ == "__main__":
    main()
