def Convert (string):
    li = list(string.replace(", ", " ").replace(",", " ").split(" "))
    return li

def CalculateMean(list):
    counter = 0
    mean = 0.0
    myTotal = 0
    for counter in range(len(list)):
        myTotal = myTotal + int(list[counter])
        counter += 1
    print("Total is: " + str(myTotal))
    mean = myTotal/counter
    return mean

inputString = input("Please enter a list of numbers: ")
print("Mean is: " + str(CalculateMean(Convert(inputString))))
