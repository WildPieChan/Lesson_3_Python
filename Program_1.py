import random

def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only integer numbers. Try again...")
    return number

def CreateRandomArray(length):
    array = []
    for i in range(length):
        number = random.randint(-11, 11)
        array.append(number)
    return array

def AmountOfArrayNumbers(array):
    amount = 0
    for i in array:
        amount += i
    return amount

n = InputNumber("Array creating... Enter length of array: ")
numbersData = CreateRandomArray(n)
print(numbersData)
numbersData = numbersData[1::2]
print("Sorting array... Only odd positions remain...")
print(numbersData)
print(f"Amount of lefted numbers: {AmountOfArrayNumbers(numbersData)}")
