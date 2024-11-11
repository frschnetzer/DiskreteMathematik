def main():
    def babylon(x):
        a = x    
        b = 1
        while (a*a - x) > 0.0001:
            a = 1/2 * (a + b)
            b = x /a
            print(a)
        
    babylon(10.0)

    def babylon_2(x):
        a = x    
        i = 0
        while (a*a - x) > 0.0001:
            a = (a +x /a) /2
            i += 1
        return (a, i)
    print(babylon_2(10))

main()