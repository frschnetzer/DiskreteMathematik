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
    m = 1 # alpha
    n = -1 # beta
    a,b = diffs.pop() # get the last two elements of list and write them into a and b. removing also these elements from list

    for x,y in reversed(diffs): # now we let d = m *a + n*b be true in each iteration, 
        if y == a: # here we check if a or b was changed in this step
            b = x
            m = m - n # decrease the multiplyer of a (as n is negative)
        else: # here y need to be b... so a was changed in this step
            a = x
            n = n - m # decreast the muliplyer of b (a n is negative)
    return [d, [m, a, n, b]]
 
print(extggT(8, 11))