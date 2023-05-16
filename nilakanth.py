import time

def nilakanth(n):
    suma = 3
    licznik = 2
    znak = 1

    stStart = time.time()
    for i in range(n):
        suma = suma + (znak * (4 / (licznik * (licznik + 1) * (licznik + 2))))
        znak *= -1
        licznik += 2
    stStop = time.time()
    
    return [suma, (i + 1), (stStop - stStart)]