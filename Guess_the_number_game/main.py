import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

## Function to set the number of attempts based on user choice of easy/hard difficulty levels.
def play_mode():
    while True:
        difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Incorrect input.")

## While loop to re-run the program if the user wants to keep playing the game after first game is over.
play_on = True
while play_on:
    num_tries = play_mode()
    computer_number = random.randint(1, 100)

    for i in range(0, num_tries):
        print(f"You have {num_tries} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        num_tries -= 1
        if guess == computer_number:
            print(f"You got it! The number was {computer_number}.")
            break
        elif guess > computer_number:
            print("Too high.")
        else:
            print("Too low.")

    if num_tries == 0:
        print(f"You lost. The number was {computer_number}.")

    play_again = input("Want to play again? Type Y or N: ").lower()
    if play_again == "n":
        play_on = False