def main():
    def primeFactor(n): #kanonische primfactoren von n
        c = 2
        result = []
        while n > 1:
            while True:
                if n % c == 0:
                    result.append(c)
                    n //= c
                    break
                c += 1
        return result
    print(primeFactor(4200))
main()