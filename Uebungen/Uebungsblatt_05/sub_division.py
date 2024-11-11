def main():
    def subtraction_division(frac1, frac2):
        a = frac1[0]
        b = frac2[0]
        n = 0
        if (frac1[1] == frac2[1]): #gleichnamiger bruch
            n = frac1[1]            
        else:
            c = frac1[1]
            d = frac2[1]
            n = (c* d)
            a *= d
            b *= c
        return [(a - b), n]
       
    def subtraction_division_short(frac1, frac2):        
        n = 0
        if (frac1[1] == frac2[1]): #gleichnamiger bruch
            n = frac1[1]            
        else:            
            n = (frac1[1] * frac2[1])
            frac1[0] *= frac2[1]
            frac2[0] *= frac1[1]
        return [(frac1[0] - frac2[0]), n]        

    print(subtraction_division([3,4], [2,4]))   
    print(subtraction_division([2,3], [1,5]))  
    print(subtraction_division_short([2,3], [1,5]))  
main()