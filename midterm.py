# 1
# import numpy as np
# import pandas as pd
# df = pd.DataFrame(np.random.randn(4, 4), index=[1, 2, 3, 4], columns=['a', 'b', 'c', 'd'])
# print(df)
#
#
# value_index = df['c'][3]  # Accessing column 'c' and then row index 3
# value_loc = df.loc[3, 'c']
# value_iloc = df.iloc[2, 2]  # Indexing starts from 0, so row 3 is index 2 and column 'c' is also index 2
#
# print(value_index, value_loc, value_iloc)

# 2

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(-10, 10, 0.1)
# y = x ** 2 + 2 * x + 3
#
# plt.plot(x, y)

# 7

# from matplotlib import pylab as plt
# import pandas as pd
# import pandas_datareader.data as web
# import datetime
# import yfinance as yfin
#
# yfin.pdr_override()
#
# today = datetime.datetime.today()
# formatted_date = today.strftime("%Y-%m-%d")
# df1 = web.DataReader('AAPL', start='2024-01-01', end=formatted_date)
# df1.index = pd.to_datetime(df1.index)
#
# num_rows = df1.shape[0] # using tuples
# print(num_rows) # it has 80 rows
#
# columns = df1.columns
# print(columns) # outputs Index(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], dtype='object')
#
# highest_value_apr4 = df1.loc['2024-04-04']['High'].max() # simple use of max
# print(highest_value_apr4) # outputs 171.9199981689453
#
# plt.figure(figsize=(10, 5)) # Initializing a new figure
# plt.plot(df1['Close']) # This column contains the closing stock prices, which will be plotted on the y-axis
# plt.xlabel('Date') # setting axis titles
# plt.ylabel('Price')
# plt.show() # showing

# 8
#
# import numpy as np
#
# a = np.arange(0, 12)
# # continue here
#
# a = a.reshape(4, 3)
#
# # should start from 1 and step by 5
# a = a * 5 + 1
#
# print(a)

# 6
import random


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    def __gt__(self, other):
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __eq__(self, other):
        return self.rank == other.rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        cards = []
        # iterate over all ranks and suits, create a card and add it to the list
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                card = Card(rank, suit)
                cards.append(card)
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        # shuffles the cards in the deck
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)


class Hand:
    def __init__(self, deck):
        # deck is shuffled before
        cards = []
        for i in range(5):
            cards.append(deck.cards[i])
        self._cards = tuple(cards)

    def __str__(self):
        return str(self._cards)

    @property
    def cards(self):
        return self._cards

    @property
    def is_flush(self):
        suit = self._cards[0].suit
        for i in range(1, 5):
            if self._cards[i].suit != suit:
                return False
        return True

    @property
    def is_pair(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 2:
                return True
        return False

    @property
    def is_3_kind(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 3:
                return True
        return False

    @property
    def is_4_kind(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 4:
                return True
        return False

    @property
    def is_full_house(self):
        return self.is_3_kind and self.is_pair

    @property
    def is_2_pair(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        ranks = set(ranks)
        return len(ranks) == 3 and not self.is_3_kind

    def sort_hand(self):
        cards = list(self.cards)
        cards.sort()
        print(f"sorted hand is: {cards}")

    @property
    def is_straight(self):
        cards = list(self.cards)
        cards.sort()
        distance = Card.RANKS.index(cards[4].rank) - Card.RANKS.index(cards[0].rank)
        return distance == 4 and not self.is_pair and not self.is_3_kind

precision = tries = 100
i = 0
while True:
    i = i + 1
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand.is_straight:
        tries -= 1

    if tries == 0:
        break

probability = precision/i * 100
print(f"The odds of getting a straight are {probability}%")


class Point:

    def __init__(self, x, y):

        self.x = x

        self.y = y



    def __str__(self):

        return f"({self.x}, {self.y})"



    def __repr__(self):

        return self.__str__()



    def distance_origin(self):

        return (self.x**2 + self.y**2)**0.5



    def __gt__(self, other):

        return self.distance_origin() > other.distance_origin()



class ColoredPoint(Point):

    def __init__(self, x, y, color):

        super().__init__(x, y)  # Call to the superclass (Point) constructor

        self.color = color



    def __str__(self):

        return f"{super().__str__()} in color {self.color}"

    def is_flush(self):
        suit = self._cards[0].suit
        return all(card.suit == suit for card in self._cards[1:])
