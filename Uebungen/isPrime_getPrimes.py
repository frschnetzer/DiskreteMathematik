def main():
    def isPrime(n): #primitive function to determine if n is prime
        if n <= 1:
            return False
        for i in range(2,n): #range = iterator, produces values when used
            if(n % i == 0):
                return False
        return True

    def getPrimes(n):
        p = []
        for i in range(n+1):
            if isPrime(i):
                p.append(i)
        return p
    
    print(getPrimes(100))

main()