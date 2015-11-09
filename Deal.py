import random

SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8",
         "9", "10", "Jack", "Queen", "King"]
CARDS = 52
CARDS_PER_HAND = 13
PLAYER = 0

def main():
    North = []
    East = []
    South = []
    West = []


    # Create a deck as a list of integers from 0 to 51
    deck = list(range(CARDS))
    # Shuffle the cards
    random.shuffle(deck)
    # Shuffle again, because once is never enough!
    random.shuffle(deck)

    # Pop a cart from the top of the deck, deal to each player, increment until player has 13 cards.

    i = 0
    while i < CARDS_PER_HAND:
        card = deck.pop()
        North.append(card)
        North.sort()
        i += 1
        # print(North)
    for i in range(len(North)):
        i = [RANKS[deck.pop(1) % CARDS_PER_HAND], 'of', SUITS[deck.pop(1) // CARDS_PER_HAND], ]
        print(i)
        #print("\n".join(map(str, North)))

    #
    #
    #
    #
    #
    #
    print("East was dealt:")
    print("---------------")
    i = 0
    while i < CARDS_PER_HAND:
        card = deck.pop()
        print(RANKS[card % CARDS_PER_HAND], "of", SUITS[card // CARDS_PER_HAND])
        i += 1
    print()
    print("South was dealt:")
    print("---------------")
    i = 0
    while i < CARDS_PER_HAND:
        card = deck.pop()
        print(RANKS[card % CARDS_PER_HAND], "of", SUITS[card // CARDS_PER_HAND])
        i += 1
    print()
    print("West was dealt:")
    print("---------------")
    i = 0
    while i < CARDS_PER_HAND:
        card = deck.pop()
        print(RANKS[card % CARDS_PER_HAND], "of", SUITS[card // CARDS_PER_HAND])
        i += 1


## can be returned from the deal function
main()
