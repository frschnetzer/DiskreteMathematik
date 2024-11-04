def CalculateProduct(a,b):
    product =  (a * b) % 256 # 256 becaus 8-bit arithmetic
    return bin(product)[2:]

print(CalculateProduct(186, 25))