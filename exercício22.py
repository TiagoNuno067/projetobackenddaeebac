# Solicita o valor da prestação em atraso ao usuário
valor_original = float(input("Digite o valor da prestação em atraso (R$): "))

# Aplica o acréscimo de 10%
valor_com_acrescimo = valor_original * 1.10

# Aplica o desconto de 10% sobre o valor acrescido
valor_final = valor_com_acrescimo * 0.90

# Calcula o prejuízo do comerciante
prejuizo_comerciante = valor_original - valor_final

# Apresenta os resultados formatados
print(f"\n--- Resumo da Operação ---")
print(f"Valor original da prestação: R$ {valor_original:.2f}")
print(f"Valor após o acréscimo (10%): R$ {valor_com_acrescimo:.2f}")
print(f"Valor final a pagar (com 10% de desconto): R$ {valor_final:.2f}")
print(f"Prejuízo do comerciante: R$ {prejuizo_comerciante:.2f}")