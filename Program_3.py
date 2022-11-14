import random

def CreateRandomArray():
    array = []
    length = random.randint(3, 11)
    for i in range(length):
        number = random.uniform(1.5, 9.5)
        array.append(round(number, 2))
    return array

def SmallestLargestRemainders(array):
    sortedArray = []
    resultArray = []
    for i in array:
        sortedArray.append(round(i % 1, 2))
    max = sortedArray[0]
    min = sortedArray[0]
    for i in sortedArray:
        if i > max:
            max = i
        if i < min:
            min = i
    resultArray.append(round(min, 2))
    resultArray.append(round(max, 2))
    return resultArray

numbersData = CreateRandomArray()
print(numbersData)
numbersData = SmallestLargestRemainders(numbersData)
result = str(numbersData[1] - numbersData[0])
print(int(result[2:]))