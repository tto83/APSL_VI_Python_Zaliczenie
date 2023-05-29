import time
from dokladnosc import dokladnosc

def nilakanth():
    suma = 3
    licznik = 2
    znak = 1

    print("\nPrzyblizenie Pi metoda Nilakanth'a")
    n = int(input('Podaj zadana liczbe powtorzen (zalecana  ~10): '))

    stStart = time.time()
    for i in range(n):
        suma = suma + (znak * (4 / (licznik * (licznik + 1) * (licznik + 2))))
        znak *= -1
        licznik += 2
    stStop = time.time()
    
    return [suma, dokladnosc(suma),(i + 1), (stStop - stStart)]