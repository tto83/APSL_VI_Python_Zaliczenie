from time import time

def brouncker(n):
    suma = 2

    stStart = time()
    while n >= 0:
        suma = ((2 * n + 1) * (2 * n + 1)) / (2 + suma)
        n -= 1
    
    wynik = 4 / (1 + suma)
    stStop = time()
    
    return [wynik, (n + 1), (stStop - stStart)]

print(brouncker(10000))