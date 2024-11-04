from sympy import prime, factorint, mod_inverse

p = prime(50)
q = prime(54)
n = p*q
phi = (p -1) * (q-1)
print(p, q, n, phi, factorint(phi))

e = 7*11*13
d = mod_inverse(e,phi)
print(e, d)

def crypt(M, e, n):
    return M**e%n
print(crypt(8262, e, n))