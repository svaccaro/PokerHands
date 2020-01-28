#!/usr/bin/python

import enum
import requests
from collections import Counter

# to do:

class HandTypes(enum.Enum):
    RoyalFlush = 1
    StraightFlush = 2
    FourOfAKind = 3
    FullHouse = 4
    Flush = 5
    Straight = 6
    ThreeOfAKind = 7
    TwoPair = 8
    Pair = 9
    HighCard = 10
    Undefined = 11

class Deck:
    # new
    def __init__(self):
        #resp = requests.get("https://deckofcardsapi.com/api/deck/new/")
        resp = APIComm.get("https://deckofcardsapi.com/api/deck/new/")
        self.deckId = resp['deck_id']
        self.countRemaining = resp['remaining']
    # shuffle returns all cards and shuffles
    def shuffle(self):
        shuffleURL = 'https://deckofcardsapi.com/api/deck/{}/shuffle/'.format(self.deckId)
        resp = APIComm.get(shuffleURL)
        self.countRemaining = resp['remaining']
    def draw(self, count):
        drawURL = 'https://deckofcardsapi.com/api/deck/{}/draw/?count={}'.format(self.deckId, count)
        resp = APIComm.get(drawURL)
        self.countRemaining = resp['remaining']
        hand = Hand(resp['cards'])
        return hand

class Hand:
    def __init__(self, cardlist):
        self.cards=[]
        for card_data in cardlist:
            self.cards.append(Card(card_data))
        self.valueCounter = Counter(card.number for card in self.cards)
        self.suitCounter = Counter(card.suit for card in self.cards)
    def toConsole(self):
        string = ', '.join(' OF '.join((c.value, c.suit)) for c in self.cards)
        return string
    # classify hand. only designed for 5 card hands.
    def classify(self):
        if len(self.cards) != 5:
            return HandTypes.Undefined
        maxValueCount = max(self.valueCounter.values())
        totalSuitCount = len(self.suitCounter)
        isStraight = (maxValueCount == 1) & (max(self.valueCounter.keys())-min(self.valueCounter.keys()) == 4)
        topCard = max(self.valueCounter.keys())

        # classification order is highest -> lowest, return when match is found
        if (isStraight and totalSuitCount==1):
            if topCard == 14:
                return HandTypes.RoyalFlush
            else:
                return HandTypes.StraightFlush
        elif maxValueCount == 4:
            return HandTypes.FourOfAKind
        elif (maxValueCount == 3 and len(self.valueCounter) == 2):
            return HandTypes.FullHouse
        elif totalSuitCount == 1:
            return HandTypes.Flush
        elif isStraight:
            return HandTypes.Straight
        elif maxValueCount == 3:
            return HandTypes.ThreeOfAKind
        elif maxValueCount == 2:
            if len(self.valueCounter)==3:
                return HandTypes.TwoPair
            else:
                return HandTypes.Pair
        else:
            return HandTypes.HighCard

class Card:
    numberLookup = {"0": 10, "JACK": 11, "J": 11, "QUEEN": 12, "Q": 12, "KING": 13, "K": 13, "ACE": 14, "A": 14}
    suitLookup = {"D":"DIAMONDS", "C":"CLUBS", "S":"SPADES", "H":"HEARTS"}

    def __init__(self, carddata):
        if isinstance(carddata, str):
            self.code = carddata
            self.value = carddata[0]
            self.suit = self.suitLookup[carddata[1]]
        elif isinstance(carddata, dict):
            self.value = carddata['value']
            self.suit = carddata['suit']
            self.code = carddata['code']
        else:
            raise ValueError

        # Assign numeric value to card
        if self.value in self.numberLookup:
            self.number = self.numberLookup[self.value]
        else:
            try:
                self.number = int(self.value)
            except ValueError:
                print('Invalid card: {}'.format(carddata))
                raise

class APIComm:
    def __init__(self):
        pass
    def get(url):
        resp = requests.get(url)
        if(resp.status_code != 200):
            raise requests.ConnectionError("GET request unsuccessful. Status Code {}".format(resp.status_code))
        return resp.json()
