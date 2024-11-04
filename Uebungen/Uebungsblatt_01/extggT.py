# Linearkombination ggT(a,b) = alpha * a + beta * b
def extggT(a,b):
    diffs = [] # here we store the differences betwenn the single values
    while a != b :
        if a < b:
            a,b = b,a # switch of variables
        diffs.append([a,b])
        a = a-b

    # now calculate m and n, s.t. (sodass) d = m*a + n*b
    d = a # this is the ggT
    m = 1
    n = -1
    a,b = diffs.pop() # last element in diffs incl. removing

    for x,y in reversed(diffs): # now we let d = m *a + n*b be true in each iteration
        if y == a: # here we check if a or b was changed in this step
            b = x
            m = m - n # decrease the multiplyer of a (as n is negative)
        else: # here y need to be b... so a was changed in this step
            a = x
            n = n - m # decreast the muliplyer of b (a n is negative)
    return [d, [m, a, n, b]]
 
print(extggT(400, 225))