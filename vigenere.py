from sys import argv
from cs50 import get_string


def main():
    
    if len(argv) != 2:
        print("incorrect usage")
        exit(1)
    
    cipher = argv[1].lower()
    key = list()
    for i in range(len(cipher)):
        if cipher[i].islower():
            key.append(ord(cipher[i]) - 97)
        else:
            print("argv incorrect")
            exit(1)
    
    text = get_string("plaintext:  ")
    print("ciphertext: ", end="") 
    i = 0
    for c in text:
        case = False
        i = i % len(key)
        if c.isupper():
            case = True
        
        c = c.lower()
        
        if c.islower():
            c = ord(c)
            c = c + key[i]
            if c > 122:
                c = 97 + (c - 123)
            c = chr(c)
            i += 1
            
        if case:
            c = c.upper()
        
        print(c, end="")

    print()
    
    
if __name__ == "__main__":
    main()