def list_sort(myList):
    for number in myList:
        if myList.count(number) == 1:
            return number
    if myList:
        return myList[0]
    else:
        return None


