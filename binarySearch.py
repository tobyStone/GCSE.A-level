def binarySearch(useItem, useNumberList):
    found = False
    bottom = 0
    top = len(useNumberList) + 1
    while bottom <= top and not found:
        middle = ((bottom + top)//2)
        if useNumberList[middle] == useItem:
            found = True
        elif useNumberList[middle] < useItem:
            bottom = middle + 1
        else:
            top = middle - 1
    return found    


numberList = [1, 2, 4, 7, 18, 29]
item = int(input("please enter the number you are looking for: "))
isItFound = binarySearch(item, numberList)
if isItFound:
    print("Your number is in the list.")
else:
    print("Your number is not in the list.")
