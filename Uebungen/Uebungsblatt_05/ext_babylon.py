def babylon_2(x, tolerance):
        a = x    
        i = 0
        while (a*a - x) > tolerance: #bsp: 0.0001
            a = (a + x /a) /2
            i += 1
            print(f"a = {a}, b = {x/a}")
        return (a, i)
    
print("Enter tolerance: ")
input_tolerance = float(input())
print(babylon_2((1+5**0.5)/2, input_tolerance))