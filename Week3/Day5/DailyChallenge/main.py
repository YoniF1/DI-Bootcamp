#For Part 1  - the quiz - please see quiz.md in the same directory

import random

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def name(self):
        return(f"{self.value} of {self.suit}")

class Deck():
    def __init__(self):
        self.cards = []

    def deck(self):
        card_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        card_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for i in range(1, 53):
            self.cards.append(Card(random.choice(card_suit), random.choice(card_value)))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return(self.cards.pop())
    
deck = Deck()
deck.deck()
print(len(deck.cards))
print(deck.deal().name())
print(len(deck.cards))



    


        