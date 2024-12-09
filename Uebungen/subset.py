def subset(A, B):
    for a in A:
        if a not in B:
            return False
    return True
A = {1,2,3,4} 
B = {3,4,5}
print(subset(A,B))