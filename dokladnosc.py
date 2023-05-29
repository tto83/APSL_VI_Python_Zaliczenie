def dokladnosc(pi = 3.14, pi_str = '14159265358979323'):
    wynik = 0
    
    temp = f'{(pi % 1):.17f}'[2:]
    
    for i in range(len(temp)):
        if pi_str[i] == temp[i]:
            wynik += 1
        else:
            break
    
    return wynik