import random
from time import time

def monteCarlo(punkty):
    licznik_okr = 0
    licznik_kw = 0

    stStart = time()
    for i in range (punkty):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        odl = (x ** 2) + (y ** 2)

        if odl <= 1:
            licznik_okr += 1
        
        licznik_kw += 1

        pi = 4 * (licznik_okr / licznik_kw)
    stStop = time()

    return [pi, punkty, (stStop - stStart)]