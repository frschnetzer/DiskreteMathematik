def main():
    def caesarDec(msg, key):
        result = ""
        for c in msg: # get every character in msg
            encChar = chr((ord(c) - ord('A') - key) % 54 + ord('A')) # get number from Unicode table
            result += encChar
        return result
    
    print(caesarDec('lepps', 4))

main()