n = int(input('Digite um numero:')) 
fato = 1

while n > 1:
    fato *= n
    n -= 1

print(f'O fatorial é {fato}')