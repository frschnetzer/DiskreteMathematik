def average(quantityA, quantityB):
    averageSet = set()
    for b in quantityB:
        if b in quantityA:
            averageSet.add(b) # when element is in both, add to set
    return averageSet

quantityA = {1,2,3,4}
quantityB = {3,4,5}
print(f"Durschnitt: {average(quantityA, quantityB)}")

def average_with_built_in(quantityA, quantityB):
    return quantityA & quantityB

print(f"Durchnitt mit built in: {average_with_built_in(quantityA, quantityB)}")