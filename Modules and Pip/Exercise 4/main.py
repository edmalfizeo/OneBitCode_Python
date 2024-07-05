import random

random_number = random.randint(1, 20)
live = 5
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 20.\n")
while live > 0:
    guess = int(input("Take a guess: "))
    if guess == random_number:
        print(f"Good job! You guessed my number in {5 - live + 1} guesses!")
        break
    elif guess < random_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    live -= 1
    if live == 0:
        print(f"Sorry, you ran out of guesses. The number was {random_number}.")
        break