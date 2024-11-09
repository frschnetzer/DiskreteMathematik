from sympy import gcd

def main():
    def kleinsterTerm(frac): #[a,b] = a/b
        zaehler = frac[0]
        nenner = frac[1]
        if zaehler < 0 and nenner < 0: # when both numbers are negative, make positive
            zaehler = abs(zaehler)
            nenner = abs(nenner)
        if nenner < 0: # when divider is negative, make positive and make numerator negative
            zaehler *= -1
            nenner = abs(nenner)
        ggT = gcd(zaehler, nenner) #get ggT
        return [zaehler // ggT, nenner // ggT]

    def multiplicate_divisions(frac1, frac2):
        a, b = frac1[0], frac1[1]
        c, d = frac2[0], frac2[1]
        multiplication = [(a * c), (b * d)]
        return kleinsterTerm(multiplication)

    print(multiplicate_divisions([3,5],[4,6])) # (3*4)/(5*6) = 12/30 => /6 = 2/5