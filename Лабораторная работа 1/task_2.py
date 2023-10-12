# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
numberPagesInBook = 100
numberLinesPerPage = 50
numberSymbolsPerLine = 25
symbolWeight = 4

volumeInBytes = int(volume * 1024 * 1024)

countOfBooks = volumeInBytes // (numberPagesInBook * numberLinesPerPage * numberSymbolsPerLine * symbolWeight)

print("Количество книг, помещающихся на дискету:", countOfBooks)
