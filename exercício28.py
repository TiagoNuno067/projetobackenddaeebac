mamifero = str(input('É mamífero?')).strip().upper()

if mamifero == 'SIM':
    quadrupede = str(input('É quadrupede?')).strip().upper()

    if quadrupede == 'SIM':
        carniforo = str(input('É carniforo?')).strip().upper()
        herbivoro = str(input('É herbivoro?')) .strip().upper()

        if carniforo == 'SIM' and herbivoro == 'NÃO':
            print('O animal escolhido foi leão.')

        elif carniforo == 'NÃO' and herbivoro == 'SIM':
            print('O animal escolhido foi cavalo.')

    elif quadrupede == 'NÃO':
        bipede = str(input('É bípede?')).strip().upper()

        if bipede == 'SIM':
            oniforo = str(input('É oniforo?')) .strip().upper()
            frutivoro = str(input('É frútivoro?')).strip().upper() 

            if oniforo == 'SIM' and frutivoro == 'NÃO':
                print('O animal escolhido foi homem.')

            elif oniforo == 'SIM' and frutivoro == 'SIM':
                print('O animal escolhido foi macaco.')

        elif bipede == 'NÃO':
            voadores = str(input('É um voador?')).strip().upper()
            aquaticos = str(input('É aquático?')).strip().upper()

            if voadores == 'SIM' and aquaticos == 'NÃO':
                print('O animal escolhido foi morcego.')

            elif voadores == 'NÃO' and aquaticos == 'SIM': 
                print('O animal escolhido foi baleia')

elif mamifero == 'NÃO':
    aves = str(input('É uma ave?')).strip().upper()

    if aves == 'SIM':
        nãovoador = str(input('É não voador?')).strip().upper()

        if nãovoador == 'SIM':

            tropicais = str(input('É tropical?')).strip().upper()
            polares = str(input('É polar?')).strip().upper()

            if tropicais == 'SIM' and polares == 'NÃO':
                print('O animal escolhido foi avestruz')

            elif tropicais == 'NÃO' and polares == 'SIM':
                print('O animal escolhido foi pinguim.')

        elif nãovoador == 'NÃO':
            nadadoras = str(input('É nadador?')).strip().upper()
            de_rapina = str(input('É de rapina?')).strip().upper()

            if nadadoras == 'SIM' and de_rapina == 'NÃO':
                print('O animal escolhido foi pato.')

            elif nadadoras == 'NÃO' and de_rapina == 'SIM':
                print('O animal escolhido foi Águia')

    elif aves == 'NÃO':
        reptil = str(input('É um réptil?')).strip().upper()

        if reptil == 'SIM':
            casco = str(input('Tem casco?')).strip().upper()
            carniforo = str(input('É carnívoro?')).strip().upper() 
            sem_patas = str(input('É sem patas?')).strip().upper() 

            if casco == 'SIM' and carniforo == 'NÃO' and sem_patas == 'NÃO':
                print('O animal escolhido foi tartaruga.')

            elif casco == 'NÃO' and carniforo == 'SIM' and sem_patas == 'NÃO':
                print('O animal escolhido é crocodilo.')

            elif casco == 'NÃO' and carniforo == 'NÃO' and sem_patas == 'SIM':
                print('O animal escolhido foi cobra.')