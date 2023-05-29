from math import sqrt, pow
from time import time
from dokladnosc import dokladnosc

def silnia(n):
    wynik = 1 if n == 0 else (n * silnia(n - 1))
    return wynik

def ramanujan():
    suma = 0
    licznik = 0
    zm = (sqrt(8) / 9801)  # 2√2/(99)^2

    print("\nPrzyblizenie Pi metoda Ramanujan'a")
    eps = int(input('Podaj zadana ilosc miejs po przecinku (zalecana 17): '))

    stStart = time()
    while True:
        temp = zm * (silnia(4 * licznik) / pow(silnia(licznik), 4)) * ((26390 * licznik + 1103) / pow(396, 4 * licznik))
        suma += temp

        if (abs(temp) < (10 ** (-eps))):
            break

        licznik += 1
    stStop = time()
    
    return [(1 / suma), dokladnosc(1 / suma), (licznik + 1), (stStop - stStart)]