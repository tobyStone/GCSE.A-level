import random, os, time
JAPANESE_NUMBERS = {1:'ICH', 2:'NI', 3:'SAN', 4:'SHI', 5:'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart, al@inventwithpython.com

In this traditional Japanese dice game. Two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

You bet on the result.

If you want to quit at any time, just press 'q'.

You have 50 coins in your purse. How much will you bet?
''')

purse = 50
while True: #main loop

        #quit game
 #   if input('>').upper() == 'Q':
 #       print("Goodbye")
 #       time.sleep(3)
 #       os._exit(1)

    #place bet
    while True:
        pot = input('>')
        if pot.upper() == 'Q':
            print("Thanks for playing!")
            time.sleep(1)
            os._exit(1)
        elif not pot.isdecimal():
            print('Please enter a number')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            #This is a valid bet
            pot = int(pot) # Convert pot to an integer
            break #Exit loop once a valid bet is placed.

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print("The dealer swirls the cup and you hear the rattle of dice")
    print("The dealer slams the cup on the floor, still covering the")
    print("dice and asks for your bet.")
    print()
    print(" CHO (even) or HAN (odd)?")

    #Let the player bet cho or han:
    while True:
        bet = input('>').upper()
        if bet == 'Q':
            print("Thanks for playing!")
            time.sleep(1)
            os._exit(1)
        elif bet != 'CHO' and bet != 'HAN':
            print("Please enter either 'CHO' or 'HAN'.")
            continue
        else:
            break

    #Reveal the dice results
    print("The dealer lifts the cup to reveal:")
    print(" ",JAPANESE_NUMBERS[dice1], "-",JAPANESE_NUMBERS[dice2])
    print(" ",dice1,"-",dice2)

    #Determine if the player has won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    #Display the bet results:
    if playerWon:
        print("You won! You take ", (pot//10) * 9, " coins.")
        purse = purse + ((pot//10) * 9) #The house fee is 10%
        print("You now have ", purse, "coins. How much do you bet on this round?")
    else:
        purse = purse - pot
        print("You lost! You lose ", pot, "coins. How much do you bet on this round?")

    #Check if the player has run out of money:
    if purse == 0:
        print("You have run out of money!")
        print("Thanks for playing!")
        time.sleep(3)
        os._exit(1)