capacidade = float(input('Digite a capacidade:'))
litros = float(input('Quantos litros abasteceu:'))
quilometragem = float(input('Quantos quilõmetros percorreu:'))

consumo = quilometragem / litros

print(f'A capacidade do tanque é {capacidade:.1f} Litros')
print(f'O consumo efetuado é {consumo}Km/l')