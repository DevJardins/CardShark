#CardShark 
#A blackjack game written in Python - based on Basic Rules for BlackJack & eventual added card counting tool/assistance

#card array for value store of each card type
cards = ["\U00002660","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","King","Queen","Jack"]

#array variables, for data store against multiplier
ace_card = cards[0]
two_card = cards[1]
three_card = cards[2]
four_card = cards[3]
five_card = cards[4]
six_card = cards[5]
seven_card = cards[6]
eight_card = cards[7]
nine_card = cards[8]
ten_card = cards[9]
king_card = cards[10]
queen_card = cards[11]
jack_card = cards[12]

#Initialize variable that holds the total amount of cards in a single playable deck
totalDeck = cards * 4


#value store for deck multiplier - undefined integer
deckValue = int()


#user input for deck value
deckValue = int(input("enter the total amount of decks that you would like to play from 1 to 8 : "))

#while loop for proper deck calculation

while True:
    if (deckValue > 8) or (deckValue < 0):
        deckValue = int(input("Please enter a different number:"))
    break
else:
    print('You have selected', deckValue, 'decks')
    break

#Deck to play
playDeck = totalDeck * deckValue