def main():
    x = (1,2)
    print(type(x), x == (2,1))

    print(x[0])
    firstArgument = lambda t: t[0] # anonyme funktion alternative: def firstArg(x): return x[0] firstArg(x)
    print(firstArgument(x))


    # map wendet eine funktion auf alle Elemente an und liefert einen Iterator.
    # List macht dann wider eine Liste darau
    print(list(map(lambda x: x**2, [1,2,3]))) # funktion wie f(x) = x²
    # all: schaut ob alle werte den Wahrheitswert true haben
    print(all([True, True, True]))

    # prüfen ob ein Argument nur tupel enthält

    def onlyTupels(s):
        return (all(map(lambda x: type(x) is tuple, s)))
    
    print(onlyTupels([(1,2), (2,4), (23,9)])) # True
    print(onlyTupels([(1,2), (2,4), (23,9)], 1)) # False, weil letztes kein tupel
main()