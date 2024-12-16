def union(quantityA, quantityB):
    copyOfA = quantityA
    for b in quantityB:
        if b not in quantityA: # when an element in b is not in a, add to copy of a
            copyOfA.add(b)
    return copyOfA

quantityA = {1,2,2,3,4}
quantityB = {3,4,5}
print(f"Vereinigung: {union(quantityA, quantityB)}")

def union_with_built_in(quantityA,quantityB):
    return quantityA | quantityB
print(f"Vereinigung mit pyhton built in: {union_with_built_in(quantityA, quantityB)}")