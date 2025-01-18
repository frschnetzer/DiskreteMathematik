# frozensubset == freeze the list and make it unchangable
# | is pythons set-union (Vereinigung)

for x in frozenset( {1,2,3}):
    print(frozenset([x]) | frozenset({10}))

frozenset({1,10})
frozenset({2,10})
frozenset({10,3})

def combs(L,k):
    if k == 0:
        yield frozenset()
    else:
        for x in L:
            for P in combs(L-{x}, k-1):
                yield frozenset([x]) | P

print(list(combs(set({1,2,3}), 2)))

# Alle Teilmengen der größe n von N
# Achtung! sehr ineffizient ist!!
def fixedSizeSubsets(n):
    k = n
    seen = set() # menge, an schon gesehenen elementen
    while True:
        for s in combs(set(range(k)), n):
            if not s in seen:
                yield s
                seen.add(s)
        k += 1
i = 5 # wie viele Elemente aus N
for mySet in fixedSizeSubsets(4):
    i -= 1
    print(list(mySet))
    if i <= 0:
        break