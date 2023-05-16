import time

def leibniz(n):
    suma = 0
    dzielnik = 1
    stStart = time.time()   

    for i in range(n):
        if i % 2 == 0:
            suma += 4 / dzielnik
        else:
            suma -= 4 / dzielnik
    
        dzielnik += 2

    stStop = time.time()    
    
    return [suma, (i + 1), (stStop - stStart)]