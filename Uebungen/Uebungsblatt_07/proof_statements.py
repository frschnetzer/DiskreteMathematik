# A teilmenge A
# oder A teilmgenge B

quantityA = {1,2,3}
quantityB = {2,3}
quantityC = {1,3,4}

def proof_reflection(quantityA, quantityB):
    for a in quantityA:
        if a not in quantityB:
            return False
    return True

print(f"Reflectiv für A von A: {proof_reflection(quantityA, quantityA)}")
print(f"Reflectiv für A von B: {proof_reflection(quantityA, quantityB)}")
print(f"Reflectiv für B von A: {proof_reflection(quantityB, quantityA)}")

def proof_transitive(quantityA, quantityB, quantityC):
    if(proof_reflection(quantityA, quantityB)) and (proof_reflection(quantityB, quantityC)):
        return True
    return False

print(f"Transitive für A, B und C {proof_transitive(quantityA, quantityB, quantityC)}")

def proof_antisymmetrie(quantityA, quantityB): # TODO überarbeiten!
    if (proof_reflection(quantityA, quantityB) and proof_reflection(quantityB, quantityA)):
        return True
    return False

print(f"Antisymmetrisch für A und B: {proof_antisymmetrie(quantityA, quantityB)}")

def proof_empty_quantity(quantityA, quantityB):
    if quantityA - quantityB == set():
        return True
    return False

print(f"Leere Menge und nicht 0: {proof_empty_quantity(quantityA, quantityA)}")

def proof_kommutative(quantityA, quantityB):
    if quantityA | quantityB == quantityB | quantityA:
        return True
    return False

print(f"Kommutativ: {proof_kommutative(quantityA, quantityB)}")

def proof_assoziative(quantityA, quantityB, quantityC):
    if quantityA or (quantityB or quantityC) == (quantityA or quantityB) or quantityC:
        return True
    return False

print(f"Assoziantiv: {proof_assoziative(quantityA, quantityB, quantityC)}")

def proof_distributive(quantityA, quantityB, quantityC):
    if quantityA or (quantityB and quantityC) == (quantityA or quantityB)and (quantityA or quantityC):
        return True
    return False
print(f"Distributivität: {proof_distributive(quantityA, quantityB, quantityC)}")

def proof_deMorgan(quantityA, quantityB, quantityC):
    if quantityA | (quantityB or quantityC) == (quantityA | quantityB) and (quantityA | quantityC):
        return True
    return False

print(f"De Morgan: {proof_deMorgan(quantityA, quantityB, quantityC)}")