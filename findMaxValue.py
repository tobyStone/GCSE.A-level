myList = [6, 9, 1, 27, 2, 42]

note = 0

    for counter in range(len(myList)):
        if (myList[counter] > note):
            note = myList[counter]

print("Max value is", str(note))    
