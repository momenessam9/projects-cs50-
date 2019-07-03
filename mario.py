
height = int(input("height: "))
while True:
    if height > 0 and height <= 8:
        break
    else:
        height = int(input("height: "))
        
i = height - 1
while (i != -1):
    
    for k in range(i):
        print(" ", end="")
        
    for j in range(height-i):
        print("#", end="")
    i -= 1
    print()
    