#this program simulates a fortune cookie giving six different fortunes
#a random number is given by the randint function

import random

print("Welcome to the random weather generator!")


answer = random.randint(1,6)

if answer == 1:

    print("Things are good weatherwise this week.")

elif answer == 2:

    print("Things are bad weatherwise this week.")

elif answer == 3:

    print("Things are average weatherwise this week.")

elif answer == 4:

    print("It's snowing.")

elif answer == 5:

    print("Storm! CRASH! BANG!")

else:

    print("You have no idea what the weather is, you stay inside, close the curtains, and stay under the covers!")

















colour = input("Please enter the colour of the traffic lights: ").upper()
if colour == "GREEN":
    print("You can cross...")
else:
    print("Please wait where you are.")

