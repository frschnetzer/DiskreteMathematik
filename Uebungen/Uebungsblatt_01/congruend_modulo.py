def congruendModulo(a, b, n):
    # true if a and b are kongruent mod n
    if(a % n == b % n):
        return True
    else:
        return False
    
print(congruendModulo(2,7,5))

def CongruentModulo(a, b, n):
    return a % n == b % n # returns boolean

print(CongruentModulo(201, 101, 19))