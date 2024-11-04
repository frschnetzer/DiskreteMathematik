def Dec2Bin(decimalNumber): 
    binaryNumber = 0 #intitializing variable to store the binary result, will serve as starting point
    binaryPosition = 1 #current power of 2 / position of the binary
    while decimalNumber > 0: #continues as long decimalNumber is greater than 0
        binaryNumber = binaryNumber + (decimalNumber % 2) * binaryPosition #calculate the remainder of decimalNumber and adds to binaryNumber multiplied by the current power (shifts bit to current position)
        decimalNumber //= 2 #removing the least significant bit
        binaryPosition *= 10 #increasing the power of 2 for the next iteration / setting the correct position of the binaryNumber
    return binaryNumber

print("Dec to bin:", Dec2Bin(255))

# dec to binary
print(format(90, "b"))