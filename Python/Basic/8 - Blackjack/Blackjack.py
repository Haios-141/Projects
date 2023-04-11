import random
from art import logo
from os import system, name

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list_of_cards):
    """Return the total score of a list of cards.\n
    Returns a 0 if there's a Blackjack
    """
    num_of_cards = len(list_of_cards)
    score = sum(list_of_cards)

    if num_of_cards == 2 and score == 21:
        return 0

    if score > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)

        return sum(list_of_cards)
    else:
        return score

def compare(user_score, computer_score):
    if user_score == 0 and computer_score == 0:
        print("It's a tie. Both players have Blackjack.")
    elif computer_score == 0:
        print("You lose, opponent has Blackjack 😱")
    elif user_score == 0:
        print("You win with a Blackjack 😂")
    elif user_score > 21:
        print("You lose 😢. You went over 21.")
    elif computer_score > 21:
        print("You win 😁. Opponent went over 21.")
    elif user_score > computer_score:
        print("You win 😃")
    elif user_score == computer_score:
        print("It's a draw 🙃")
    else:
        print("You lose 😢")

def verify_response(prompt):
    response = input(prompt).lower()
    while response != "y" and response != "n":
        response = input(prompt).lower()

    return response

def print_results(user_cards, user_score, computer_cards):
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    
### Comment out on Replit
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
    
##---------------------- End of functions ---------------------------------------##

prompt = "Do you want to play a game of Blackjack? Type 'y' or 'n': "
play_game = verify_response(prompt)

while play_game == "y":
    clear()
    print(logo)
    
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    user_turn = "y"

    while True:
        cards_in_hand = len(user_cards)
        
        if cards_in_hand == 0: # Only enter this if-statement if the game has just started
            for _ in range(0, 2):
                user_cards.append(deal_card())
                computer_cards.append(deal_card())
            
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            
            if user_score == 0 or user_score > 21 or computer_score == 0 or computer_score > 21:
                break
        else:
            if user_turn == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            
                if user_score > 21 or user_score == 0:
                    computer_score = calculate_score(computer_cards)
                    break
            else:
                computer_score = calculate_score(computer_cards)
                
                if computer_score > 21 or computer_score == 0:
                    break
                else:
                    while computer_score < 17:
                        computer_cards.append(deal_card())
                        computer_score = calculate_score(computer_cards)
                    break # break out of the inner loop -- while True:

        print_results(user_cards, user_score, computer_cards)

        prompt = "Type 'y' to get another card, type 'n' to pass: "
        draw_card = verify_response(prompt)

        if draw_card == "n":
            user_turn = "n"

    print_results(user_cards, user_score, computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)
    
    prompt = "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    play_game = verify_response(prompt)
    
    if play_game == "n":
        break

print("\nGoodbye 👋")