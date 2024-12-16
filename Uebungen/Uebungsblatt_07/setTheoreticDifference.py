def setTheoreticDifference(quantityA, quantityB):
    copyOfA = quantityA
    for b in quantityB:
        if b in quantityA:
            copyOfA.remove(b)
    return copyOfA

quantityA = {1,2,3,4}
quantityB = {3,4,5}
print(f"Mengentheoretische Dirrerenz: {setTheoreticDifference(quantityA, quantityB)}")

def setTheoreticDifference_with_built_in(quantityA, quantityB):
    return quantityA / quantityB

print(f"Mengentheoretische Dirrerenz mit built in: {setTheoreticDifference(quantityA, quantityB)}")
