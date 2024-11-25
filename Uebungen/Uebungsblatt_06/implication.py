def main():
    def implication(a,b):
        if a:
            if b:
                return True
            return False
        else:
            return True
        
    print(implication(True, True))
    print(implication(True, False))
    print(implication(False, True))
    print(implication(False, False))

main()