# Menge der natürlichen Zahlen

def Nat():
    n = 0
    while True:
        yield n # pausiert die ausführung der Funktion
        n += 1

def viewGen(gen, n):
    c = 1
    L = []
    for x in gen:
        if c > n:
            break
        L.append(x)
        c += 1
    return L

def main():
    print(viewGen(Nat(), 10))

main()