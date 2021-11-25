############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal():
    continues = True
    handPlayer = []
    handAi = []
    def drawPlayer():
        handPlayer.append(random.choice(cards))
    def drawAi():
        handAi.append(random.choice(cards))
    while continues:
        print (logo)
        drawPlayer()
        drawPlayer()            
        drawAi()
        print (f"Your hand is {handPlayer}")
        print (f"Dealer's hand is {handAi}")
        if input("would you like to draw again? 'y' or 'n' ") == "y":
            drawPlayer()
            if 11 in handPlayer and sum(handPlayer) > 20:
                if input("Would you like your ACE to be 1 or 11? ") == '1':
                    handPlayer.remove(11)
                    handPlayer.append(1)
            drawAi()
            if sum(handAi) < 17:
                drawAi()
            cls()
            print (logo)
        else:
            drawAi()
            if sum(handAi) < 17:
                drawAi()
            cls()
            print(logo)
        if sum(handPlayer) > 21:
            print (f"Your hand is {handPlayer}, you lost.")
            print (f"Dealer's hand is {handAi}")
        elif sum(handAi) > 21:
            print (f"Your hand is {handPlayer}, you won!")
            print(f"Dealer's hand is {handAi}")
        elif sum (handPlayer) < sum(handAi):
            print (f"Your hand is {handPlayer}, you lost.")
            print (f"Dealer's hand is {handAi}")
        elif sum(handPlayer) == sum(handAi):
            print (f"Your hand is {handPlayer}")
            print (f"Dealer's hand is {handAi}")
            print ("It's a draw!")
        else:
            print (f"Your hand is {handPlayer}, you won!")
            print (f"Dealer's hand is {handAi}")
        if input("Would you like to play again? 'y' or 'n' ") == 'y':
            cls()
            handPlayer = []
            handAi = []
            deal()
        continues = False
deal()