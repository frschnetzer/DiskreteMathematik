def main():
    def allquantor(A, M):
        for x in M:
            if not A(x):
                return False
            return True
        
    def ExistenuquantorTwo(A, m1, m2):
        for i in m1:
            for j in m2:
                if A(i, j):
                    return True
        return False

    # Aussage: Es gibt eine Zahl die mal sich selber gleich die Zahl hoch 2 ist
    a_1 = lambda x: x*x == x**2
    m = {1,2,3,4,5,6,7,8,9}

    print(allquantor(a_1, m))

    # Aussage: Es gibt zwei natürliche Zahlen x und y, sodass x + y = 10
    a_2 = lambda x, y: x + y == 10
    m1 = {1,2,3,4,5,6} # menge
    m2 = {1,2,3,4,5,6}

    print(ExistenuquantorTwo(a_2, m1, m2))
main()