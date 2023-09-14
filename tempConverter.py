def userInp():
    inpVal = int(input("Please enter 1 to convert C to F and 2 to convert F to C: "))
    entVal = int(input("Please enter your value: "))

    if inpVal == 1:
        convCtoF(entVal)
    else:
        convFtoC(entVal)

def convCtoF(entVal):
    tempVal = entVal*9/5 + 32
    print("This is {0} F".format(tempVal))
          
def convFtoC(entVal):
    tempVal = (entVal -32) *5/9
    print("This is {0} C".format(tempVal))

userInp()