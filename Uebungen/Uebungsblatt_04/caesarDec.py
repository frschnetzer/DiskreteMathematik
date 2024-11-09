def main():
    def caesarDec(msg, key):
        result = ""
        for char in msg: # get every character in msg
            if char.isupper():  # Check if the character is uppercase
                enc_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            else:  # If lowercase, convert to uppercase, encrypt, and convert back
                enc_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            result += enc_char
        return result
    
    print(caesarDec('lepps', 4))

main()