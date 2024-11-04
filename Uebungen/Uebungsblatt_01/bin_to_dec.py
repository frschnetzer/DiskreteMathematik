def Bin2Dec(binaryNumber):
    decimalNumber = binaryNumber[0] #get first element of binaryNumber
    for number in binaryNumber[1:]: #iterating throught binaryNumber except the first (0,1) element of the list. Starts at the second element
        decimalNumber = decimalNumber * 2 + number #multiplying the first element with 2 and adding the current element of the binary list
    return decimalNumber

print("Bin to dec:", Bin2Dec([1,1,0,1]))

#bin to dec
print(int('11100', 2))