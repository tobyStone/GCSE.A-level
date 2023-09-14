def LinearSearch(searchList, searchInt):
  #  counter = 0
    for counter in range(len(searchList)):
        found = False
        if searchInt == int(searchList[counter]):
            found = True
            if found == True:
                return counter            
            else:
                return False
        counter += 1

listToSplit = input("Please enter a list of numbers: ")
myList = listToSplit.split(" ")
myInt = int(input("Please enter a number you are trying to find in the list: "))
indexValue = LinearSearch(myList, myInt)
if indexValue is None:
    print("Number not found.")
else:
    print("Item found at index: " + str(indexValue) + 1)
