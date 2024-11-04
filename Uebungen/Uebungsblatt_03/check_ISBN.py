def checkISBN(digits):
    multiplicator = 1
    checksum = digits[-1] # get last element from string
    result = 0
    for i in digits[:-1]: # iterating through digits and removing the last element our checksum 
        result += int(i)* multiplicator # casting i as number so we can calculate with the multiplicator
        multiplicator += 1
    if int(checksum) == result % 11:
        return True
    else:
        return False
    
print(checkISBN("1484211774"))        