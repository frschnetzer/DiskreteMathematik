def main():
    def complex_conjugate(a,b):
        return a +(b * -1)
    
    result = complex_conjugate(3,4j)
    print(f"Ergebnis: {result}")
    result = complex_conjugate(5,7j)
    print(f"Ergebnis: {result}")
main()