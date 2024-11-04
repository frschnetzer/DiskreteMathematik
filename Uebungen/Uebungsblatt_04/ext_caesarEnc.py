def main():
    def caesarEnc(msg, key):
        result = ""
        for c in msg: # get every character in msg
            encChar = chr((ord(c) - ord('A') + key) % 54 + ord('A')) # get number from Unicode table
            result += encChar
        return result
    
    print(caesarEnc('HAlLO', 4))

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