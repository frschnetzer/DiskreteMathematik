def main():
    def complex_substract(a,b,c,d):
        real = (a - c)
        imag = (b - d)
        return real + imag
    
    result = complex_substract(2,3j,2,-2j)
    print(f"Ergebnis: {result}")
    result = complex_substract(8,4j,5,2j)
    print(f"Ergebnis: {result}")
main()