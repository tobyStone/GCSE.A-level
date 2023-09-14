###
binaryNumber = input("Please input a four digit binary number: ")
print((int(binaryNumber[0])*8) + (int(binaryNumber[1])*4) + (int(binaryNumber[2])*2) + (int(binaryNumber[3])))
###

binary = input("Please enter the 8 digit binary code: ")

binlength = len(binary)



x = 0
y =1
ans = 0
while x != 8:
    if binlength > 8:
        print("Invalid code\n to big")
        break
    elif binlength < 8:
        print("Invalid code\n too small")
        break
    else:
        if binary[x:y] =="1":
            if x == 0:
                ans = ans + 2**7
            elif x == 1:
                ans = ans + 2**6
            elif x == 2:
                ans = ans + 2**5
            elif x == 3:
                ans = ans + 2**4
            elif x == 4:
                ans = ans + 2**3
            elif x == 5:
                ans = ans + 2**2
            elif x == 6:
                ans = ans + 2**1
            else:
                ans = ans + 2**0
        else:
            ans = ans + 0
        x = x+1
        y = y+1
print(ans)


binaryNumber = input("Please enter a binary number of any length: ")
power = len(binaryNumber2) - 1


value = 0
for i in binaryNumber:
    if i =='1':
        value = value + (2**power)
    power = power -1
print(value)


binary = input("enter a four digit binary number: ")

power = len(binary) - 1

value = 0
for i in binary:
    if i == '1':
        value = value + power **2
    power = power -1

print(value)


#print("8 cats have 4 legs each")
#legs = str(8*4)
#print("The cats have " + legs, "legs")

#print("9 cats have 4 legs each")
#print("In total the cats have", 9*4, "legs")

#yourName = input("please enter your name: ")
#favFood = input("please enter your favourite food: ")
#print("Your name is:", yourName, "and your favourite food is:", favFood)


#number = int(input("Please enter a number to be doubled: "))
#numberDoubled = number * 2
#print("Your doubled number is:", numberDoubled)
 
 

#foodOne = "Cheese"
#foodTwo = "Onion"
#print(foodOne)
#print("My favourite crisps are {0} and {1}".format(foodOne, foodTwo))
        




       
 


#def LinearSearch(searchList, searchInt):
#    counter = 0
#    for counter in range(len(searchList)):
#        found = False
#        if searchInt == int(searchList[counter]):
 #           found = True
  #          if found == True:
   #             return counter
#            else:
#                return False
#        counter += 1
#listToSplit = input("Please enter a list of numbers: ")
#myList = listToSplit.replace(", ", " ").replace(",", " ").split(" ")
#myInt = int(input("Please enter a number you are trying to find in the list: "))
#indexValue = LinearSearch(myList, myInt)
#if indexValue is None:
#    print("Number not found.")
#else:
#    print("Item found at index: " + str(indexValue))













#import turtle
#myTurtle = turtle.Turtle()





#def drawRegularPolygon(sides, length):
#    myTurtle.pendown()
#    angle = 360/sides
#    for i in range(0, sides):
#        myTurtle.forward (length)
#        myTurtle.right (angle)

#drawRegularPolygon(3, 100)

















        
        
        
        
        
        
        
        
        
        
        
        
        
#        value = value + (2**power)
#    power -= 1

#print(value)


#rowLength = 4
#columnLength = 6
#myArray = [[86 for row in range (rowLength)] for column in range(columnLength)]
#myArray[0][3] = 12
#print(myArray)






#myList = [2,4,6, 42,31]
#counter = 0
#note = myList[0]
#for counter in range(len(myList)):
#    if myList[counter] > note:
#        note = myList[counter]
#    counter = counter + 1
#print("Max value is", str(note))

#print(max(myList))



