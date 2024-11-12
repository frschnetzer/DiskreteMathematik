from sympy import gcd

def main():
    def kleinsterTerm(frac): #[a,b] = a/b = 10/-20 -> 1/-2 -> -1/2
        zaehler = frac[0]
        nenner = frac[1]
        # if zaehler < 0 and nenner < 0: # when both numbers are negative, make positive
        #     zaehler = abs(zaehler)
        #     nenner = abs(nenner)
        if nenner < 0: # when divider is negative, make positive and make numerator negative
            zaehler *= -1
            nenner = abs(nenner)
        ggT = gcd(zaehler, nenner) #get ggT
        return [zaehler // ggT, nenner // ggT]
    
    print(kleinsterTerm([10,-20]))
    print(kleinsterTerm([-10,50]))
    print(kleinsterTerm([0,10]))

main()