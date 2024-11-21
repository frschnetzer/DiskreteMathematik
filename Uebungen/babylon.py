def main():
    def babylon(x):
        a = x    
        b = 1
        while (a*a - x) > 0.0001:
            a = 1/2 * (a + b)
            b = x /a
            print(a)
        
    babylon(10.0)

    def babylon_2(x, tolerance):
        a = x    
        i = 0
        while (a*a - x) > tolerance: #bsp: 0.0001
            a = (a + x /a) /2
            i += 1
            print(f"a = {a}, b = {x/a}")
        return (a, i)
    
    print("Enter tolerance: ")
    input_tolerance = input()
    print(babylon_2((1+5**5)/2, input_tolerance))

main()