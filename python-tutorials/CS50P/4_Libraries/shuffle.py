from random import random, shuffle

cards = ["Jack", "Queen", "King"]
print(random() * 10)
# shuffle the cards
shuffle(cards)
for card in cards:
    print(card)
