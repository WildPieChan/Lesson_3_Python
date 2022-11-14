import random

def CreateRandomArray():
    array = []
    length = random.randint(3, 11)
    for i in range(length):
        number = random.randint(-11, 11)
        array.append(number)
    return array

def MultiplicationOfPairs(array):
    arrayOfMult = []
    i = 0
    while i < (len(array) / 2):
        multiplication = 0
        multiplication = (array[i] * array[-i - 1])
        print(f"{array[i]} x {array[-i - 1]}")
        arrayOfMult.append(multiplication)
        i += 1
    return arrayOfMult

numbersData = CreateRandomArray()
print(numbersData)
print(MultiplicationOfPairs(numbersData))
