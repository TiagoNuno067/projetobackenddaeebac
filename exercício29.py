# Passo 1: Criamos uma função para calcular o MDC (Máximo Divisor Comum)
# Usaremos o Algoritmo de Euclides, que é a forma mais rápida e eficiente.
def calcular_mdc(a, b):
    # O laço continua até que o resto da divisão (b) seja zero
    while b != 0:
        # 'a' recebe o valor de 'b', e 'b' recebe o resto da divisão de 'a' por 'b'
        a, b = b, a % b
    # Quando b for 0, o 'a' será o nosso MDC
    return a

# Passo 2: Criamos a função para calcular o MMC
def calcular_mmc(a, b):
    # Se um dos números for zero, o MMC é zero (evita erro de divisão por zero)
    if a == 0 or b == 0:
        return 0
    
    # Aplicamos a fórmula: (a * b) dividido pelo MDC de (a, b)
    # Usamos '//' para garantir que o resultado seja um número inteiro
    mmc = (a * b) // calcular_mdc(a, b)
    return mmc

# --- Programa Principal ---

# Passo 3: Pedimos os dois valores ao usuário e os convertemos para inteiros (int)
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Passo 4: Chamamos a função do MMC passando os números digitados
resultado = calcular_mmc(num1, num2)

# Passo 5: Exibimos o resultado na tela
print(f"O Mínimo Múltiplo Comum (MMC) de {num1} e {num2} é: {resultado}")
