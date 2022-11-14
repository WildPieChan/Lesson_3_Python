def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only integer numbers. Try again...")
    return number

def intoBinary(number):
    binarynumber = ""
    if (number != 0):
        while (number >= 1):
            if (number % 2 == 0):
                binarynumber = binarynumber + "0"
                number = number / 2
            else:
                binarynumber = binarynumber + "1"
                number = (number - 1) / 2
    else:
        binarynumber = "0"
    return "".join(reversed(binarynumber))


n = InputNumber("Enter any integer number: ")
n = intoBinary(n)
print(f"Your number in binary: {n}")
