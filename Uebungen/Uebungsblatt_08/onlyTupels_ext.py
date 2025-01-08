def rightUnique(f):
    for x1, y1 in f:
        for x2, y2 in f:
            if x1 == x2 and y1 != y2:
                return False
    return True
        
def onlyTupels(s): # lösung, wenn nur 2 tupel sein dürfen
        for elements in s:
            if len(elements) == 2:
                return (all(map(lambda x: type(x) is tuple, s)))
        return False

def onlyTupels_new(s):
     if all(map(lambda x: type(x) is tuple, s)):
        for element in s:
            if len(element) != 2:
                return False
        return True
     return False

def isFunction(f):
    return onlyTupels(f) and rightUnique(f)

print(isFunction([(1,2), (2,4), (23,9), (11,2)]))
print(isFunction([(1,2), (2,4), (23,9), (11,2), 1]))
print(isFunction([(1,2), (2,4), (23,9), (11,2)]))
print(isFunction([(1,2), (2,4)]))
print(isFunction([(1,2), (2)]))
print(isFunction([(1,2), 4]))

print(onlyTupels_new([(1,2), (2,4), (23,9), (11,2)]))
print(onlyTupels_new([(1,2), (2,4), (23,9), (11,2), 1]))
print(onlyTupels_new([(1,2), (2,4), (23,9), (11,2)]))
print(onlyTupels_new([(1,2), (2,4)]))
print(onlyTupels_new([(1,2,3), (2,5)]))
print(onlyTupels_new([(1,2), 4]))