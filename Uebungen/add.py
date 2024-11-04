from sympy import gcd

def main():
    def kleinsterTerm(frac): #[a,b] = a/b
        zaehler = frac[0] #get first element
        nenner = frac[1]
        ggT = (zaehler, nenner) #get ggT
        return [zaehler // ggT, nenner /ggT]

    def add(frac1, frac2):
        z1 = frac1[0]
        n1= frac1[1]
        z2 = frac2[0]
        n2 = frac2[1]
        return kleinsterTerm([(z1* n2) + z2*n1, n1*n2])
    print(add([3,5], [4,6]))
main()