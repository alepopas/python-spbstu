numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbersWithoutNone = numbers[:4] + numbers[5:]
sumOfNumbers = sum(numbersWithoutNone)
lenOfNumbers = len(numbers)
missedItem = sumOfNumbers/lenOfNumbers
numbers[4] = missedItem

print("Измененный список:", numbers)
