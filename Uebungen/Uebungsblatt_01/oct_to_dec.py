def Oct2Dec(octalNumbers):
    number = octalNumbers[0] #initializing the first digit of octalNumbers, will serve as starting point
    for oct in octalNumbers[1:]: # looping through all digits in octalNumbers except the first one
        number = number * 8 + oct #is multiplied by 8 to shift the existing decimal value one place to the left. The current octal digit is added to number,  multiplying it by 8^(index of the digit)
    return number

print("Oct to dec:", Oct2Dec([6, 4, 5]))