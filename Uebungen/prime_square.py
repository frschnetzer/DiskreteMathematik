# Alle Primzahlen deren Quadrat < 10000
import sympy
 
X = set()
for n in range(2,101): # 100**2 = 10000
    if sympy.isprime(n) and n*n < 10000:
        X.add(n)
X
# das geht auch einfacher
A = range(2,101)
D = {n for n in A if sympy.isprime(n) and n*n < 10000 }
print(D)