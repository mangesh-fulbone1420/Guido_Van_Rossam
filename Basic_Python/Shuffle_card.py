import random,itertools
#suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck=list(itertools.product(range(1,14),['Hearts','Diamonds','Clubs','Spades']))

random.shuffle(deck)
print("The Shuffled Card is :",deck)

for i in range(5):
    print(deck[i][0], "of", deck[i][1]) 
