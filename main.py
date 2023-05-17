from brouncker import brouncker
from gaussLegendre import gaussLegendre
from leibniz import leibniz
from monteCarlo import monteCarlo
from nilakanth import nilakanth
from ramanujan import ramanujan

def main():
    print(brouncker(10000000))
    print(gaussLegendre(1000))
    print(leibniz(10000))
    print(monteCarlo(1000000))
    print(nilakanth(10))
    print(ramanujan(100))
main()