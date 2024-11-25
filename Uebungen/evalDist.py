def main():
    p = True
    q = False
    r = True
    not (p | q)

    print(p | (q & r))
    print((p & q) | (p & r))
    

    a = []
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                a.append([p,q,r])
    print(a)
    
    # a = [[True, True, True],
    #       [True, True, False],
    #       [True, False, True],
    #       [True, False, False],
    #       [False, True, True],
    #       [False, True, False],
    #       [False, False, True],
    #       [False, False, False]]
    
    def evalDist(p,q,r):
        return (p | (q & r))  == (p | q) & (p | r)
 
    a[0]
    evalDist(a[0][0], a[0][1], a[0][2])     
 
    for x in a:
        if not evalDist(x[0], x[1], x[2]):
            print(str(x[0]), str(x[1]), str(x[2]))
        print("False")
        break

    evalDist(True, False, False)
main()