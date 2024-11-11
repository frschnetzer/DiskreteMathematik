def main():
    def div_division(frac1, frac2):
        a, c = frac1[0], frac1[1]
        b, d = frac2[0], frac2[1]
        return [(a * d), (c * b)]
    print(div_division([2,3], [5,7]))
main()