# program to shuffle deck of the cards
import itertools, random

deck_card=list(itertools.product(range(1,14),['spade','heart','diamond','club']))
random.shuffle(deck_card)
print("The selected cards are: ")
for i in range(6):
    print(deck_card[i][0]," of ",deck_card[i][1])