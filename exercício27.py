pais1 = str(input('Primeiro pais:')).strip().upper()
pais2 = str(input('Segundo pais:')).strip().upper()
pais3 = str(input('Terceiro pais:')).strip().upper()

if pais1 == 'ESTADOS UNIDOS' and pais2 == 'CHINA' and pais3 == 'JAPÃO':
    print(f'{pais1}: Ouro: 40. Prata: 44. Bronze: 42. Total: 126 ')
    print(f'{pais2}: Ouro: 40. Prata: 27. Bronze: 24. Total: 91') 
    print(f'{pais3}: Ouro: 20. Prata: 12. Bronze: 13. Total: 45')

elif pais1 == 'AUSTRALIA' and pais2 == 'FRANÇA' and pais3 == 'HOLANDA':
    print(f'{pais1}: Ouro: 18. Prata: 19. Bronze: 16. Total: 53 ')
    print(f'{pais2}: Ouro: 16. Prata: 26. Bronze: 22. Total: 64') 
    print(f'{pais3}: Ouro: 15. Prata: 7. Bronze: 12. Total: 34')

elif pais1 == 'REINO UNIDO' and pais2 == 'COREIA DO SUL' and pais3 == 'ITALIA':
    print(f'{pais1}: Ouro: 14. Prata: 22. Bronze: 29. Total: 65 ')
    print(f'{pais2}: Ouro: 13. Prata: 9. Bronze: 10. Total: 32') 
    print(f'{pais3}: Ouro: 12. Prata: 13. Bronze: 15. Total: 40')

elif pais1 == 'ALEMANHA' and pais2 == 'BRASIL' :
    print(f'{pais1}: Ouro: 12. Prata: 13. Bronze: 8. Total: 33 ')
    print(f'{pais2}: Ouro: 3. Prata: 7. Bronze: 10. Total: 20') 

else:
    print('Esses países não estavam nos jogos olímpicos de Paris 2024.')