def najDokladnosc(dane):
    wynik = {}
    for key, value in dane.items():
        wynik[key] = value[1]
    
    wynik = sorted(wynik.items(), key=lambda x: x[1], reverse=True)

    print('Najwieksza dokladnosc:')
    i=1
    for key, value in wynik:
        print(f'{i}. {key}: {value}')
        i += 1

    cont = input('\nNacisnij ENTER aby kontynuowac\n')

def najIter(dane):
    wynik = {}
    for key, value in dane.items():
        wynik[key] = value[2]
    
    wynik = sorted(wynik.items(), key=lambda x: x[1])

    print('Najmniejsza ilosc iteracji:')
    i=1
    for key, value in wynik:
        print(f'{i}. {key}: {value}')
        i += 1

    cont = input('\nNacisnij ENTER aby kontynuowac\n')

def najCzas(dane):
    wynik = {}
    for key, value in dane.items():
        wynik[key] = value[3]
    
    wynik = sorted(wynik.items(), key=lambda x: x[1])

    print('Najmniejszy czas:')
    i=1
    for key, value in wynik:
        print(f'{i}. {key}: {value:.8f}')
        i += 1

    cont = input('\nNacisnij ENTER aby kontynuowac\n')