from brouncker import brouncker
from gaussLegendre import gaussLegendre
from leibniz import leibniz
from monteCarlo import monteCarlo
from nilakanth import nilakanth
from ramanujan import ramanujan
from wyniki import wyniki
from ranking import *
from eksportCSV import eksportCSV
import os


algorytmy = {}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    cls()

    algorytmy['Brouncker'] = brouncker()
    algorytmy['Gauss Lagendre'] = gaussLegendre()
    algorytmy['Leibniz'] = leibniz()
    algorytmy['Monte Carlo'] = monteCarlo()
    algorytmy['Nilakanth'] = nilakanth()
    algorytmy['Ramanujan'] = ramanujan()

    cls()
    wyniki(algorytmy)

    cls()
    najDokladnosc(algorytmy)
    najIter(algorytmy)
    najCzas(algorytmy)

    cls()
    pyt = input('Czy zapisac wyniki do pliku wyniki.csv? [T/N]:')
    if pyt.upper() == 'T':
        eksportCSV(algorytmy, 'wyniki.csv')

main()