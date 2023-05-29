from time import time
from dokladnosc import dokladnosc

def brouncker():
    suma = 2

    print("\nPrzyblizenie Pi metoda Williama Brounckera'a")
    n = int(input('Podaj zadana liczbe powtorzen (zalecana  > 500k): '))

    stStart = time()
    licznik = n
    while n >= 0:
        suma = ((2 * n + 1) * (2 * n + 1)) / (2 + suma)
        n -= 1
    
    wynik = 4 / (1 + suma)
    stStop = time()
    
    return [wynik, dokladnosc(wynik), licznik, (stStop - stStart)]

