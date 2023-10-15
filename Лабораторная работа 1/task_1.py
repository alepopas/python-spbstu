numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

missingItemIndex = numbers.index(None)
numbersWithoutNone = numbers[:missingItemIndex] + numbers[missingItemIndex+1:]
sumOfNumbers = sum(numbersWithoutNone)
lenOfNumbers = len(numbers)
missedItem = sumOfNumbers/lenOfNumbers
numbers[missingItemIndex] = missedItem

print("Измененный список:", numbers)
