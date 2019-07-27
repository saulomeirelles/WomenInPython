# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:12:44 2019

@author: tseng
"""

# The Basics

'''
Data Types --> string int
Variable
operators symbols ---> =, ==, !=, <=, >=, <, >, and, or, not  
Class
object
list
For loop
while loop
if else statement

'''

# build blackjack Card Game

suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
suits_symbols = ['♠', '♦', '♥', '♣']
suits = ['\u2660','\u2666','\u2665','\u2663']

# setup Playing cards

class Card:

    card_values = {
        'A': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10,'K': 10
    }
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        #self.points = self.card_values[rank]
        
    def printCard(self):
        return self.rank + self.suit
    
    def getCardValue(self):
        return self.card_values[self.rank]

suits = ['\u2660','\u2666','\u2665','\u2663']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = []
    
# Create and populate 1 deck of cards
for s in suits:
    for r in ranks:
        card = Card(s, r)
        deck.append(card)
        
''' 
for i in range(len(suits)):
    for j in range(len(ranks)):
        card = Card(suits[i], ranks[j])
        deck.append(card)
'''

# checking if the cards are created correctly
def showCardList(cardlist):
    for i in range(len(cardlist)):
        if (i+1) % 13 != 0:           
            print(cardlist[i].printCard(), end='')
        else:
            print(cardlist[i].printCard())

showCardList(deck)

# Shuffle Cards


# game logic

