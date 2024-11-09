def main():
    def pzSieb(n):
        counter = 0
        numbers = list(range(2,n)) # list of all numbers from 2 till n
        primes = []
        c = 2
        while c*c < n:
            for k in range(c,n,c): # liste von vielfachen was c ist                
                if k in numbers:
                    numbers.remove(k) # removing all multiplicates in list
            primes.append(c)
            c = numbers[0]
            counter += 1
            if counter >= 3:
                    return F"primzahlen: {primes} + Ergebnis: {numbers}"
        return primes + numbers
    
    print(pzSieb(97))

main()