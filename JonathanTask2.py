def return_non_duplicate2(myList):
    for number in myList:
        if myList.count(number) == 1:
            return number
