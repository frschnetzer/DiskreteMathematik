from sympy import prime, mod_inverse

def main():
    # je höher die primzahlen, desto länger dauert die entschüsselung
    p = prime(2) #gibt 50 primzahl
    q = prime(4)
    n = p*q # muss > als input sein, input muss 2 kleiner sein laut definition
    phi = (p - 1) * (q - 1)

    e = 7*11*13 #(e,n) weil primzahlen, die nicht in primfaktorzerlegung in phi(n) vorkommen. e ist teilerfremd, öffentliicher schlüssel
    d = mod_inverse(e,phi) #(d,n) privater schlüssel 

    def crypt(plainInput, e, n):
        return plainInput**e%n
    encrypted = crypt(19, e, n)
    print(f"Verschlüsselt: {encrypted}")   

    def decrypt(encryptedInput, d, n):
        return encryptedInput**d%n
    decrypted = decrypt(encrypted, d, n)
    print(f"Entschlüsselt: {decrypted}")
main()
