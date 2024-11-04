def Dec2Oct(decimalNumber):
    number = 0 #initializing variable to store octal number
    decimalPosition = 1 #setting start position of decimal number
    while decimalNumber > 0: # looping as long as decimalNumber is greater than 0
        number = number + (decimalNumber % 8) * decimalPosition #modulo through 8 because octal and multiply by the correct position
        decimalNumber //= 8 #removing least significant digit from number, to get the next dec number
        decimalPosition *= 10 #multiplying to get correct position of decimal number /shifting
    return number

print("Dec to oct:", Dec2Oct(421))