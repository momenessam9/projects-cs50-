from cs50 import get_int
height = get_int("height: ")
while True:
    if height > 0 and height <= 8:
        break
    else:
        height = get_int("height: ")
        
i = height - 1
while (i != -1):
    
    for k in range(i):
        print(" ", end="")
        
    for j in range(height-i):
        print("#", end="")
    i -= 1
    print()
    