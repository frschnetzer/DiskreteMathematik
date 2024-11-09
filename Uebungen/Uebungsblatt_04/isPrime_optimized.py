import math
def main():
    def isPrime(n): #primitive function to determine if n is prime
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    print(isPrime(2))
main()