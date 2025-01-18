def ggT(a,b):
    if a > b:
        a, b = b, a   
    if a == 0:
        return b
    while a > 0: # no exit
        if a % a == 0 and b % a == 0: # when the remainder of a and b modulo divider is null we have the ggT
            return a
        a -= 1# if not null, decrement divider

print(ggT(400, 225))

# ggT Algorithm
def optimized_ggT(a, b):
    while a != b:
        if a < b:
            b = b % a # calculating with the remainder
            if b == 0: # check if b is null, we need to return the bigger value so a
                return a
        else:
            a = a % b
            if a == 0:
                return b

print(optimized_ggT(225, 400))
print(ggT(233,144))