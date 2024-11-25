def main():
    def disjunction(a,b):
        if a:
            if b:
                return True
        return False

    print(disjunction(True, True))
    print(disjunction(True, False))
    print(disjunction(False, True))
    print(disjunction(False, False))
main()