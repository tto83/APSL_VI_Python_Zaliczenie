from math import sqrt, pow
from time import time
from dokladnosc import dokladnosc

def gaussLegendre():
    an = 1
    bn = 1 / sqrt(2)
    tn = 0.25
    pn = 1

    print("\nPrzyblizenie Pi metoda Gauss'a i Legendre")
    n = int(input('Podaj zadana liczbe powtorzen (zalecana  <= 1000): '))

    stStart = time()
    for i in range(n):
        temp = an
        an = (an + bn) / 2
        bn = sqrt(temp * bn)
        tn = tn - pn * pow(temp - an, 2)
        pn *= 2
    
    wynik = pow(an + bn, 2) / (4 * tn)
    stStop = time()
    return [wynik, dokladnosc(wynik), (n), (stStop - stStart)]