from cs50 import get_string


def main():
    while True:
        number = get_string("number: ")
        if number.isdigit():
            break
        else:
            number = get_string("number: ")
    lon = len(number)
    sits = []
    while lon > 0:
        sits.append(lon - 2)
        lon -= 2
    mul = []
    reg = []
    j = 0
    for i in number:
        if j in sits:
            mul.append(str(int(i) * 2))
        else:
            reg.append(int(i))
        j += 1
    su = sum(reg)
    su1 = 0
    for i in mul:
        if len(i) > 1:
            su1 += int(i[0]) + int(i[1])
        else:
            su1 += int(i)
    final = su1 + su
    if final % 10 != 0:
        print("INVALID")
    elif len(number) == 15:
        print("AMEX")
    elif (len(number) == 13 or len(number) == 16) and int(number[0]) == 4:
        print("VISA")
    elif len(number) == 16:
        print("MASTERCARD")
    

if __name__ == "__main__":
    main()