def injective (f):
    for x1, y1 in f:
        for x2, y2 in f:
            if x1 != x2 and y1 == y2:
                return False
    return True

def rightUnique(f):
    for x1, y1 in f:
        for x2, y2 in f:
            if x1 == x2 and y1 != y2:
                return False
    return True
        
def onlyTupels(s):        
    return (all(map(lambda x: type(x) is tuple, s)))

def isFunction(f):
    return onlyTupels(f) and rightUnique(f) and injective(f)

print(isFunction([(1,2), (2,3), (3,2)]))
print(isFunction([(1,2), (2)]))
print(isFunction([(1,2), (2,3), (3,4)]))