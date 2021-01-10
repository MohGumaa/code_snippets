import random

# value = random.random()

# Generate number with decimal btw 1 and 10
value = random.uniform(1, 10)
# value = random.randint(1,6)

# greetings = ['hi', 'Hello', 'Hey', 'Hola', 'Howdy']
# value = random.choice(greetings)

colors = ['Red', 'Black', 'Green']
# Return list of 10 random number
value = random.choices(colors, k=10)
value = random.randrange(1,6)

# Make each item possiblity to pick
# value = random.choices(colors, weights=[18,18,2], k=10)

print(value)

# deck = list(range(1, 53))
# put in uorder
# random.shuffle(deck)
# print(deck)

# Chocie file unique value
# hand = random.sample(deck, k=5)
# print(hand)
