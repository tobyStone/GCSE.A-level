
# put year groups into key stages
#KeyStage = "invalid"
YearGroup = int(input("Enter Year Group: "))
if YearGroup == 1 or YearGroup == 2:
    KeyStage = 1
elif YearGroup >= 3 and YearGroup <= 6:
    KeyStage = 2
elif YearGroup >= 7 and YearGroup <= 9:
    KeyStage = 3
elif YearGroup == 10 or YearGroup == 11:
    KeyStage = 4
else: 
    print("Not a valid Year Group")
    
print("You are in Key Stage",KeyStage)




#year = 0
#keyStage = 0


#year = int(input("What Year are you? (1-11) "))
#if year == 1 or 2:
#    keyStage = 1
#elif year == 3 or year == 4 or year == 5 or year == 6:
#    keyStage = 2
#elif year == 7 or year == 8 or year ==  9:
#    keyStage = 3
#elif year == 10 or year == 11:
#    keyStage = 4
#else:
#    print("Wrong input")
#print ("Your Key stage is: ",keyStage)

#print(type("15"))