#CardShark 
#A blackjack game written in Python - based on Basic Rules for BlackJack & eventual added card counting tool/assistance

#import modules
import random 
from functions import deckCalc
from functions import AceLogic 
from functions import playerChoice
from functions import winner
from functions import dealerLogic


#Array for Card store and value
cards = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","King","Queen","Jack"]
#array variables, for data store against multiplier
cards[0] = int(1) or int(11)
cards[1] = int(2)
cards[2] = int(3)
cards[3] = int(4)
cards[4] = int(5)
cards[5] = int(6)
cards[6] = int(7)
cards[7] = int(8)
cards[8] = int(9)
cards[9] = int(10)
cards[10] = int(10)
cards[11] = int(10)
cards[12] = int(10)

#define cardChoice variable
cardChoice = str()

#total deck = 52 cards
totalDeck = cards * 4

#user input for deck value
deckValue = int(input("enter the total amount of decks that you would like to play from 1 to 8 : "))

#calculate deck size 
playDeck = totalDeck * int(deckValue)

#Display total amount of cards in deck
print('You are playing with', len(playDeck), 'cards')

#Create a random number generator for the deck
random.shuffle(playDeck)

#decrement cards from deck based on dealer and player hand
dealerHand = playDeck.pop(1)
dealerHand1 = playDeck.pop(1)
playerHand = playDeck.pop(1)
playerHand1 = playDeck.pop(1)

#Obfuscate one card in dealer hand
print('Dealer has', dealerHand, 'and an unknown card')

#Print player hand
print('Player has', playerHand, 'and', playerHand1)

#calculate total value of player hand
playerHandTotal = int()
playerHandTotal = int(playerHand) + int(playerHand1)

#calculate total value of dealer hand
dealerHandTotal = int()
dealerHandTotal = int(dealerHand) + int(dealerHand1)

#Print total value of player hand
print('Player hand total is', playerHandTotal)


#while loop for card logic
playerChoice(cardChoice, playerHand, playerHand1, playDeck)

dealerLogic(dealerHand, dealerHand1, dealerHandTotal)

winner(playerHandTotal, dealerHandTotal)


