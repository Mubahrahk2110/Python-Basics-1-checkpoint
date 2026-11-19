import random

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

number = random.randint(1, 100)
guess = 0
difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()

if difficulty == "easy":
    max_guesses = 10
elif difficulty == "medium":
    max_guesses = 7
else:
    max_guesses = 5

while guess != number and max_guesses > 0:
    guess = int(input("Enter your guess: "))
    max_guesses -= 1

    if guess > number:
        print("Your guess is too high. Guess again.")
    elif guess < number:
        print("Your guess is too low. Guess again.")
    else:
        print("Congratulations! You guessed the number correctly!")

if max_guesses == 0:
    print(f"Game over! The number was {number}.")