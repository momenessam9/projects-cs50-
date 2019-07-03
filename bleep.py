from cs50 import get_string
from sys import argv


def main():
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)
        
    rfile = open(argv[1], "r")
    words = set()
    for line in rfile:
        words.add(line.rstrip("\n"))
        
    text = get_string("What message would you like to censor?\n")
    text = text.split()

    for j in text:
        if j.lower() in words:
            for i in range(len(j)):
                print("*", end="")
            print(" ", end="")
        else:
            print(j, end="")
            print(" ", end="")
    print()


if __name__ == "__main__":
    main()
