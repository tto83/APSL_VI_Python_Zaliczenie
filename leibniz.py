def leibniz(n):
    suma = 0
    dzielnik = 1

    for i in range(n):
        if i % 2 == 0:
            suma += 4 / dzielnik
        else:
            suma -= 4 / dzielnik
    
    dzielnik += 2
    return suma

print(leibniz(1000))