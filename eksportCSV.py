import time

def eksportCSV(dane, nazwa):
    plik = open(nazwa, 'w')
    plik.write(';'.join(['Timestamp', 'Metoda', 'Pi', 'Dokladnosc', 'Iteracje', 'Czas\n']))
    timestamp = time.time()
    for key, value in dane.items():
        linia =[str(timestamp), key, str(value[0]), str(value[1]), str(value[2]), f'{value[3]}\n']
        plik.write(';'.join(linia))
    plik.close()

    print('Zapisano...')
    cont = input('Nacisnij ENTER aby kontynuowac.')
