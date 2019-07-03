from cs50 import get_int
height = get_int("height: ")
while True:
    if height > 0 and height <= 8:
        break
    else:
        height = get_int("height: ")
        
line = height 
while (line != 0):
    
    for l in range(line - 1):
        print(" ", end="")

    for j in range(height - (line - 1)):
        print("#", end="")
    
    for i in range(2):
        print(" ", end="")
        
    for k in range(height - (line - 1)):
        print("#", end="")
        
    print()
    line -= 1