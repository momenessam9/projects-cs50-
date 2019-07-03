from sys import argv

key = int(argv[1])
key = key % 26
from cs50 import get_string
text = get_string("plaintext:  ")
print("ciphertext: ", end="") 
for c in text:
    case = False
    if c.isupper():
        case = True
    
    c = c.lower()
    
    if c.islower():
        c = ord(c)
        c = c + key
        if c > 122:
            c = 97 + (c - 123)
        c = chr(c)
        
    if case:
        c = c.upper()
    
    print(c, end="")
print()
    