
"""
https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
"""
def caesarCipherEncryptor(string, key):
    # Write your code here.
    alphabet = {"a":1, "b":2,"c":3,"d":4,"e":5,
                "f":6, "d":7, "h":8,"i":9,"j":10,
                "k":11, "l":12,"m":13,"n":14,"o":15,
                "p":16, "q":17,"r":18,"s":19,"t":20,
                "u":21, "v":22,"w":23,"x":24,"y":25,"z":26
                }
    abc = "abcdefghijklmnopqrstuvwxyz"
    startIndex = alphabet[string[0]]
    index = (startIndex + key) % 26
    st = ""
    for i in range(len(string)):
        st = st + abc[index-1]
        index = (index + 1) % 26
    return st
    
inp = "xyz"
key = 2
caesarCipherEncryptor(inp, key)