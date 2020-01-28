from cardclasses import *

deck = Deck()
deck.shuffle()
# initialize empty hand
hand = None

print("""
Let's draw poker hands
\td(raw): draw a hand of 5 cards
\tb(est): get the highest poker rank of your current hand
\ts(huffle): return all cards to the deck and reshuffle
\tq(uit): quit the program""")

while True:
    user_input = input(">>> ")
    if user_input.lower() in ["q","quit"]:
        break
    elif user_input.lower() in ["s","shuffle"]:
        deck.shuffle()
        hand.cards = []
        print("Shuffled the deck")
    elif user_input.lower() in ["d","draw"]:
        drawCount = 5
        if deck.countRemaining < drawCount:
            print("Only {} cards are left in the deck. To draw a new hand, return all cards to the deck by entering shuffle.".format(deck.countRemaining))
        else:
            hand = deck.draw(5)
            print("5 card hand has been drawn: {}\n{} cards left in the deck.".format(hand.toConsole(), deck.countRemaining))
    elif user_input.lower() in ["b","best"]:
        if (hand is not None and len(hand.cards)==5):
            print(hand.classify().name.replace("_"," "))
        else:
            print("No hand available. Please draw a hand.")
    else:
        print("Unknown command")
