def powerSet(A):
    if A == set(): # wenn A leere menge ist
        yield frozenset() # gib frozenset zurück
    else:
        a = A.pop() #  entferne letzes element und speichere in a
        for X in powerSet(A): # rufe rekursiv auf, bis leere Menge
            yield X
            yield X | {a}


def finiteSubsets(): 
    k = 0   
    seen = set()
    while True:
        for s in powerSet(set(range(k))):
            if not s in seen: # wenn nicht schon existiert, speichere
                yield s
                seen.add(s)
        k += 1

def __main__():
    i = 10 # wie viele sollen angezeigt werden
    for mySet in finiteSubsets():
        i -= 1
        print(list(mySet))
        if i <= 0:
            break
__main__()
