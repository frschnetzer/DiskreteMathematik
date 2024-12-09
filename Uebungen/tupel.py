def main():
    x = (1,2)
    print(type(x), x == (2,1))

    print(x[0])
    firstArgument = lambda t: t[0]
    print(firstArgument(x))

main()