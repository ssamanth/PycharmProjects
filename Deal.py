import random

SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8",
         "9", "10", "Jack", "Queen", "King"]
CARDS = 52
CARDS_PER_HAND = 13


def main():
    # Create empty sets to be filled
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
    # Pop a card from the top of the deck, deal to each player, increment until player has 13 cards.
    # reorder the populated list, translate the int value to strings and print, respectively.
    print("North was dealt:")
    print("----------------")
    i = 0
    while i < CARDS_PER_HAND:
        card = deck.pop()
        North.append(card)
        North.sort()
        i += 1
    for i in North:
        print(RANKS[i % CARDS_PER_HAND], 'of', SUITS[i // CARDS_PER_HAND])
    print()
    print()

    print("East was dealt:")
    print("---------------")
    i = 0
    while i < CARDS_PER_HAND:
        card = deck.pop()
        East.append(card)
        East.sort()
        i += 1
    for i in East:
        print(RANKS[i % CARDS_PER_HAND], 'of', SUITS[i // CARDS_PER_HAND])
    print()
    print()

    print("South was dealt:")
    print("---------------")
    i = 0
    while i < CARDS_PER_HAND:
       card = deck.pop()
       South.append(card)
       South.sort()
       i += 1
    for i in South:
       print(RANKS[i % CARDS_PER_HAND], 'of', SUITS[i // CARDS_PER_HAND])
    print()
    print()

    print("West was dealt:")
    print("---------------")
    i = 0
    while i < CARDS_PER_HAND:
        card = deck.pop()
        West.append(card)
        West.sort()
        i += 1
    for i in West:
        print(RANKS[i % CARDS_PER_HAND], 'of', SUITS[i // CARDS_PER_HAND])


main()