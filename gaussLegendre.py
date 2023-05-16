from math import sqrt, pow
from time import time

def gaussLegendre(n):
    an = 1
    bn = 1 / sqrt(2)
    tn = 0.25
    pn = 1

    stStart = time()
    for i in range(n):
        temp = an
        an = (an + bn) / 2
        bn = sqrt(temp * bn)
        tn = tn - pn * pow(temp - an, 2)
        pn *= 2
    
    wynik = pow(an + bn, 2) / (4 * tn)
    stStop = time()
    return [wynik, (n + 1), (stStop - stStart)]