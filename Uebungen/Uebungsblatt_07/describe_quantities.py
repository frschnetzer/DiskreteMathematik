from fractions import Fraction

def describe_quantities_01():
    y1 = set()
    for x in range(1, 101):
        frac = Fraction(1, x)
        y1.add(frac)
    return sorted(y1)

def describe_quantities_02():
    y2 = set()
    for x in range(0, 21):
        y2.add(2 ** x)
    return sorted(y2)

def describe_quantities_03():
    y3 = set()
    for x in range(1,31):
        y3.add(((-1) ** x) * (x ** 3))
    return sorted(y3)

def main():
    # menge 1
    Y1 = describe_quantities_01()
    for y in Y1:
        print(y)

    # menge 2
    print(describe_quantities_02())

    # menge 3 negativen und positiven Kubikzahlen
    print(describe_quantities_03())

main()