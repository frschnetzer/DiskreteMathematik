from sympy import gcd

def main():
    def kleinsterTerm(frac): #[a,b] = a/b
        zaehler = frac[0]
        nenner = frac[1]
        ggT = gcd(zaehler, nenner) #get ggT
        return [zaehler // ggT, nenner /ggT]
    print(kleinsterTerm([10,0]))

main()