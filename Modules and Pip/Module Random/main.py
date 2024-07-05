import random
# Select a random item from a list
print(random.choice([1, 2, 3, 4, 5]))

# Select a random number between numbers
print(random.randint(1, 100))

# Select a random character in a string
print(random.choice("Hello, World!"))

# Select more than one random item from a list
print(random.sample([1, 2, 3, 4, 5], 3))
print(random.sample("Hello, World!", 3))
