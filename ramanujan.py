from math import sqrt, pow
from time import time

def silnia(n):
    wynik = 1 if n == 0 else (n * silnia(n - 1))
    return wynik

def ramanujan(eps = 8):
    suma = 0
    licznik = 0
    zm = (sqrt(8) / 9801)  # 2√2/(99)^2

    stStart = time()
    while True:
        temp = zm * (silnia(4 * licznik) / pow(silnia(licznik), 4)) * ((26390 * licznik + 1103) / pow(396, 4 * licznik))
        suma += temp

        if (abs(temp) < (10 ** (-eps))):
            break

        licznik += 1
    stStop = time()
    
    return [(1 / suma), (licznik + 1), (stStop - stStart)]