def wyniki(dane):
    print('Wyniki:')
    
    for key, value in dane.items():
        print(f'\n{key}:')
        print(f'    Obliczone Pi: {value[0]:.17f}')
        print(f'    Dokladnosc: {value[1]}')
        print(f'    Liczba iteracji: {value[2]}')
        print(f'    Czas dzialania: {value[3]:.8f}s')
    
    cont = input('Nacisnij ENTER aby kontynuowac')