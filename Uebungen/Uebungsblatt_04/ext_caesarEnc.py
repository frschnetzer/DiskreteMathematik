def main():
    def caesarEnc(msg, key):
        result = ""
        for char in msg: # get every character in msg
            if char.isupper():  # Check if the character is uppercase
                enc_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:  # If lowercase, convert to uppercase, encrypt, and convert back
                enc_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result += enc_char
        return result
    
    print(caesarEnc('HAlLOz', 2))

main()






















def main():
    def ext_caesarEnc(msg, key):
        result = ""
        for c in msg: # get every character in msg
            decChar = chr((ord(c) - ord('A') - key) % 52 + ord('A')) # get number from Unicode table
            result += decChar
        return result
    
    print(ext_caesarEnc('LEpps', 4))
main()