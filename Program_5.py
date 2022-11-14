def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only integer numbers. Try again...")
    return number

def GetFibonacci(n):
    fiboNums = []
    a, b = 1, 1
    for i in range(n):
        fiboNums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n + 1):
        fiboNums.insert(0, a)
        a, b = b, a - b
    return fiboNums

n = InputNumber("Enter length of fibonacci sequence: ")
print(GetFibonacci(n))