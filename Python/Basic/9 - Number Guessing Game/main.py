import random
from art import logo
from os import system, name


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def verify_response(prompt, selector):
    response = input(prompt).lower()

    if selector == 1:
        while response != "y" and response != "n":
            response = input(prompt).lower()
    else:
        while response != "easy" and response != "hard":
            response = input(prompt).lower()

    return response


replay = "y"
while replay == "y":
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_num = random.randint(1, 100)

    EASY = 10
    HARD = 5
    turns = 0

    prompt = "Choose a difficulty level. Type 'easy' or 'hard': "
    difficulty = verify_response(prompt, 2)

    if difficulty == "easy":
        turns = EASY
    else:
        turns = HARD

    print(f"------------- HINT: The number is: {random_num} -------------")
    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")

        while True:
            try:
                guess = int(input("Make a guess: "))
            except ValueError:
                print("Choose a number between 1 and 100.")
                continue
            else:
                break
        
        if guess > random_num:
            print("Too high.\nGuess again.")
        elif guess < random_num:
            print("Too low.\nGuess again.")
        else:
            print("\n")
            break

        print("\n")

        turns -= 1

    if turns > 0:
        print(f"You got it! The answer was {random_num}")
    else:
        print("You've run out of guesses. You Lose.")

    prompt = "Play another game? Type 'y' or 'n': "
    replay = verify_response(prompt, 1)

    if replay == "n":
        print("\nGoodbye!!! Thanks for playing.")