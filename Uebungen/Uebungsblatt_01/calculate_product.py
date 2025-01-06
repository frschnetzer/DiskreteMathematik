def CalculateProduct(a,b):
    product =  (a * b) % 256 # 256 becaus 8-bit arithmetic
    return bin(product)[2:]# gibt ergebnis ohne 0b an

print(CalculateProduct(186, 25))