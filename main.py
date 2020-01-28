from cardclasses import *

deck = Deck()
deck.shuffle()
print("""
Let's draw poker hands
\tdraw: draw a hand of 5 cards
\tbest hand: classify your best hand
\tshow hand: display your cards
\tshuffle: return all cards to the deck and reshuffle
\tquit: quit the program""")

while True:
    user_input = input(">>> ")
    if user_input.lower() == "quit":
        break
    elif user_input.lower() == "shuffle":
        deck.shuffle()
        print("Shuffled the deck")
    elif user_input.lower() == "draw":
        drawCount = 5
        if deck.countRemaining < drawCount:
            print("Only {} cards are left in the deck. To draw a new hand, return all cards to the deck by entering shuffle.".format(deck.countRemaining))
        else:
            hand = deck.draw(5)
            print("5 card hand has been drawn: {}".format(hand.toConsole()))
    elif user_input.lower() == "best hand":
        print(hand.classify())
    elif user_input.lower() == "show hand":
        print(hand.toConsole())
    else:
        print("Unknown command")
