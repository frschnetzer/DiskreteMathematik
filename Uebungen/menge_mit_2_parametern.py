# Menge mit 2 Parametern
from fractions import Fraction
B = {1,2,5}
C = {3,7,9,11}
A = set()
for n in B:
    for d in C:
        A.add(Fraction(n,d))
for a in A: 
    print(a)