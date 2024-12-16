from fractions import Fraction

def viewGen(gen, n):
    c = 1
    L = []
    for x in gen:
        if x not in L:
            if c > n:
                break
            L.append(x)
            c += 1
    return L

def Rat():
    c = 2
    while True:
        denominator = 1
        while denominator < c:
            yield Fraction(c - denominator, denominator)
            denominator += 1
        c += 1

def main():
    for q in viewGen(Rat(), 10):
        print(q)

main()