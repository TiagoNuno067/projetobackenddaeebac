print('Sapato: 50Reais. [1] dinheiro [2] cartão de crédito [3] dividir em dois [4] dividir em três')
forma_de_pagamento = int(input('Escolha a forma de pagamento:'))

if forma_de_pagamento == 1:
    preço = (10/100) * 50
    preçodesconto = 50 - preço
    print(f'Em dinheiro você vai pagar apenas R${preçodesconto:.2f}')

elif forma_de_pagamento == 2:
    preço = (5/100) * 50
    preçodesconto = 50 - preço
    print(f'No cartão você vai pagar apenas R${preçodesconto:.2f}')

elif forma_de_pagamento == 3:
    preçoparcelado = 50 / 2
    print(f'Você vai pagar R${preçoparcelado:.2f} duas vezes sem juros')

elif forma_de_pagamento == 4:
    porcento = (0.10 * 50) 
    juros = porcento + 50
    preçoparcelado = juros / 3
    print(f'Você vai pagar R${preçoparcelado:.2f} três vezes com juros de 10%')
    