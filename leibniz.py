import time
from dokladnosc import dokladnosc

def leibniz():
    suma = 0
    dzielnik = 1

    print("\nPrzyblizenie Pi metoda Leibniz'a")
    n = int(input('Podaj zadana liczbe powtorzen (zalecana  > 500k): '))

    stStart = time.time()   
    for i in range(n):
        if i % 2 == 0:
            suma += 4 / dzielnik
        else:
            suma -= 4 / dzielnik
    
        dzielnik += 2

    stStop = time.time()    
    
    return [suma, dokladnosc(suma), (i + 1), (stStop - stStart)]