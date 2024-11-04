def main():
    def caesarEnc(msg, key):
        result = ""
        for c in msg: # get every character in msg
            encChar = chr((ord(c) - ord('A') + key) % 26 + ord('A')) # get number from Unicode table
            result += encChar
        return result
    
    print(caesarEnc('HALLO', 4))

main()