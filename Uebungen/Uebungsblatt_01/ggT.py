# ggT Algorithm
def ggT(a, b):
    while a != b:
        if a < b:
            b = b - a     
        else:
            a = a - b
    return a 

print(ggT(7, 17)) 