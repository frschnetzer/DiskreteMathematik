import sympy

def main():
    def rsa_enc():
        p = sympy.prime(50) # 229
        q = sympy.prime(54) # 251
        n = p*q
        phi = (p - 1) * (q - 1)
        e = sympy.factorint(phi)

    rsa_enc()

main()