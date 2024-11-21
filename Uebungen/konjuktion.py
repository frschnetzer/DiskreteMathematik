def main():
    def konjuktion(a,b):
        if a == True:
            if b == True:
                return True
        return False
    print(konjuktion(True, True))
    print(konjuktion(True, False))
    print(konjuktion(False, True))
    print(konjuktion(False, False))
main()
    