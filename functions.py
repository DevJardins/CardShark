#Logic >> Functions

#Ace Logic
def AceLogic(dealerHand, dealerHand1, dealerHandTotal):
    if dealerHand or dealerHand1 == cards[0] and dealerHandTotal < 10:
        dealerHand = dealerHand + 11
    elif dealerHand or dealerHand1 == cards[0] and dealerHandTotal > 10:
            dealerHand = dealerHand + 1
    elif dealerHand and dealerHand1 == cards[0]:
            dealerHandTotal = 12

#Dealer Logic
def dealerLogic(dealerHand, dealerHand1, dealerHandTotal):
    while dealerHandTotal < 17:
        dealerHandTotal = dealerHandTotal + playDeck.pop(1) 
        break
        print('Dealer has', dealerHandTotal)
        if dealerHandTotal > 17:
            print('Dealer has', dealerHandTotal)
        
#while loop for proper deck calculation
def deckCalc():
        while True:
            if (deckValue > 8) or (deckValue < 0):
                deckValue = int(input("Please enter a different number:"))
            break
            if False:
                print('You have selected', deckValue, 'decks')

#function for calling player choices
def playerChoice(playerHand, playerHand1, dealerHandTotal,playDeck, cardChoice):
    cardChoice = input('Would you like to double down, hit, or stand? ')
    while True:
        if cardChoice == 'hit':
            print('You have selected', cardChoice)
            playerHand = playerHand + playerHand1 + playDeck.pop(1)
            print('Player has', playerHand)
            print('Dealer has', dealerHandTotal)
            break
        elif cardChoice == 'stand':
            print('You have selected', cardChoice)
            print('You are playing with', len(playDeck), 'cards')
            print('Dealer has', dealerHandTotal)
            break
        elif cardChoice == 'double down':
            print('You have selected', cardChoice)
            playerHand = playerHand + playDeck.pop(1)
            print('Player has', playerHand)
            print('Dealer has', dealerHandTotal)
            break
        else:
            cardChoice = input('Please enter a valid choice:')    

#function for choosing winner
def winner(playerHandTotal, dealerHandTotal):
    if playerHandTotal > dealerHandTotal:
        print('You win!')
    elif playerHandTotal < dealerHandTotal:
        print('You lose!')
    elif playerHandTotal == dealerHandTotal:
        print('Push!')
    elif playerHandTotal > 21:
        print('Player busts. Dealer wins!')
    elif dealerHandTotal > 21:
        print('Dealer busts. You win!')
    elif playerHandTotal == 21:
        print('Blackjack! You win!')
    elif dealerHandTotal == 21:
        print('Dealer has blackjack. You lose!')

