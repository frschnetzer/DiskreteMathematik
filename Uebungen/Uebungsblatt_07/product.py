def calc_product(quantityA, quantityB):
    product = set()
    for a in quantityA:
        for b in quantityB:
            product.add((a,b))
    return sorted(product)

quantityA = {1,2,3}
quantityB = {4,5}
print(calc_product(quantityA, quantityB))