aluno = float(input('Digite a nota:'))

if aluno >= 7:
    print(f'Aprovado! sua nota é {aluno}')

elif aluno >= 5 and aluno < 7:
    print(f'Recuperação! sua nota é {aluno} ')

else:
    print('Reprovado!')