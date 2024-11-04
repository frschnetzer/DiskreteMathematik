def calculate_crossum(a):
    checksumA = 0
    while a > 0:
        checksumA += a % 10
        a //= 10
    return checksumA

def iterate_crosssum(a):
    while a > 9:
        a = calculate_crossum(a)
    return a    

calculatedcrosssum = calculate_crossum(13498977)
print(calculatedcrosssum)
iterateCrosssum = iterate_crosssum(calculatedcrosssum)
print(iterateCrosssum)