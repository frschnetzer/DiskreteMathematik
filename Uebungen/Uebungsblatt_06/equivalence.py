def main():
    def equivalence(a,b):
        if a == b:
            return True
        return False
    
    print(equivalence(True, True))
    print(equivalence(True, False))
    print(equivalence(False, True))
    print(equivalence(False, False))

main()