def return_non_duplicate(myList):
    for number in myList:
        if myList.count(number) == 1:
            return number
