import random
from time import time
from dokladnosc import dokladnosc

def monteCarlo():
    licznik_okr = 0
    licznik_kw = 0


    print("\nPrzyblizenie Pi MonteCarlo")
    punkty = int(input('Podaj zadana liczbe lsowan punktow (zalecana  > 1M): '))

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

    return [pi, dokladnosc(pi), punkty, (stStop - stStart)]