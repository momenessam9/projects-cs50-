from cs50 import get_float

while True:
    left = get_float("change owed: ")
    if left > 0:
        break

cents = round(left * 100) 
i = 0
if cents // 25 != 0:
    i += cents // 25
    cents = cents % 25
if cents // 10 != 0:
    i += cents // 10
    cents = cents % 10
if cents // 5 != 0:
    i += cents // 5
    cents = cents % 5 
    
i += cents // 1

print(i)