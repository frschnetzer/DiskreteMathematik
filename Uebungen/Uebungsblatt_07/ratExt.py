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

# TODO: liste in Rat hinzufügen und dort überprüfen ob schon vorhanden
def Rat():
    c = 2
    # emptyList = []
    while True:
        denominator = 1
        while denominator < c:
            # if frac not in emptyList
            yield Fraction(c - denominator, denominator)
            denominator += 1
        c += 1

def main():
    for q in viewGen(Rat(), 10):
        print(q)

main()