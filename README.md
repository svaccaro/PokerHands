# PokerHands
Draw a 5-card hand from a deck of cards and classify it as a poker hand

*Note: This application has only been tested on Python v3.8*

### Instructions:

1. Download this repository
2. Open a Terminal (Mac) or Command Prompt (Windows) window
3. Navigate to the downloaded PokerHands folder (cd /path/to/PokerHands)
4. Run tests by entering python3 tests.py
5. Start the program by entering main.py
   - This will create a new deck and perform an initial shuffle.
   - The available options for operation will be displayed, and are as follws:
     - s or shuffle returns all cards and shuffles the deck
     - d or draw draws and displays a 5 card hand
     - b or best displays the highest ranking poker hand made by the current drawn hand
     - q or quit quits the program

### Environment assumptions:
- An internet connection is active.
- The running environment has Python 3 installed.
- Python library "requests" is installed for Python 3.
- Python library "enum" is installed for Python 3 (this is included in the standard library for v3.4+).

### Design and implementation assumptions:
- A poker hand contains exactly five cards.
- The deck consist of 52 unique cards and contains no Jokers.
- Only the most recently drawn hand can be classified.
- There is a single player who can only hold one hand at a time.
- Cards are not automatically returned to the deck when a new hand is drawn.
- Aces are high.
