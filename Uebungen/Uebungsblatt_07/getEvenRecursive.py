def getEvenRecursive():
    n = 0
    while True:
        yield n
        n += 2 # creates "list" with only even numbers


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
    print(viewGen(getEvenRecursive(), 10))
main()