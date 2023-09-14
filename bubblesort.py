def bubbleSort (myList):
    moreSwaps = True

    while moreSwaps:
        moreSwaps = False
        for element in range (len(myList)-1):
            if (myList[element]) > (myList[element + 1]):

                moreSwaps = True
                temp = myList[element]
                myList[element] = myList[element + 1]
                myList[element + 1] = temp
    return myList                

useList = [10, 1, 2, 1 , 3, 9, 7, 5, 5, 7]
print(bubbleSort(useList))
