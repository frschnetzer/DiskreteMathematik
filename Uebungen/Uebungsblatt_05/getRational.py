def main():
    def getRational(a,b,n):
        #c = a+b/2   
        #d = c+a/2     
        list = []
        while n > 0:
            x = a
            a = (a+b)/2
            b = x           
            list.append(a)
            n -= 1
        return list
    print(getRational(3.0,4.0,10))
main()