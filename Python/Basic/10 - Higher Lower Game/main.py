# import the necessary files
from art import logo, vs
from game_data import data
from random import randint
from os import system, name


def clear():
    """
    Clear the console.
    """
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def retrieve_data():
    """
    Retrieve and return a single item, which is in a dictionary form, from the 'data' list,
    and remove the item from the list upon retrieval. Returns 0 if list is empty.
    """

    list_len = len(data)

    if list_len > 0:
        rand_num = randint(0, list_len - 1)
        retrieved_data = data[rand_num]
        data.pop(rand_num)

        return retrieved_data
    else:
        return 0


def format_into_string(account):
    """
    Takes a list as an argument, and returns the entity data as a string and in a formatted order.
    """
    l_name = account["name"]
    description = account["description"]
    country = account["country"]

    first_letter = description[0].upper()

    if first_letter == "A" or first_letter == "E" or first_letter == "I" or first_letter == "O" \
            or first_letter == "U":
        article = "an"
    else:
        article = "a"

    return f"{l_name}, {article} {description}, from {country}"


def display_info(string, information, follower_count=-1):
    if follower_count == -1:
        print(f"{string}: {information}")
    else:
        print(f"{string}: {information} **Hint: {str(follower_count)}")


def verify_response(p_prompt):
    response = input(p_prompt).upper()
    while response != "A" and response != "B":
        response = input(p_prompt).upper()

    return response


def lose(p_score):
    """
    Takes a score as an argument, and displays the final score when the player loses.
    """
    print(f"Sorry, that's wrong. Final score: {p_score}")


def congratulations(p_score):
    print(f"Congratulations!!! You've reached the end of the game.\nYour final score is: {p_score}")


def end_of_game(function):
    clear()
    print(logo)
    function(score)


def get_new_info():
    """
    Get new entity information and return it as a list, with follower count at index 0, and the formatted
    information at index 1.
    """
    account = retrieve_data()

    if account != 0:
        follower_count = account["follower_count"]
        information = format_into_string(account)

        return [follower_count, information]
    else:
        return 0


def compare_answer(p_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return p_guess == "A"
    else:
        return p_guess == "B"


# ------------------ Functions End Here ------------------------------ ##

score = 0
game_round = 0

entity_A = get_new_info()
entity_B = []

print(logo)
if entity_A != 0:
    while True:
        if game_round == 0:
            follower_count_A = entity_A[0]
            information_A = entity_A[1]
            game_round = 1
        else:
            clear()
            print(logo)
            score += 1
            print(f"You're right! Current score: {score}")

            entity_A = entity_B
            follower_count_A = entity_A[0]
            information_A = entity_A[1]

        # To play the game as it is meant to, uncomment 1 and comment out 2
        # display_info("Compare A", information_A)  # 1
        display_info("Compare A", information_A, follower_count_A)  # 2
        print(vs)

        entity_B = get_new_info()

        if entity_B != 0:
            follower_count_B = entity_B[0]
            information_B = entity_B[1]

            # To play the game as it is meant to, uncomment 1 and comment out 2
            # display_info("Against B", information_B)
            display_info("Against B", information_B, follower_count_B)
        else:
            end_of_game(congratulations)
            break

        prompt = "Who has more followers? Type 'A' or 'B': "
        guess = verify_response(prompt)

        is_correct = compare_answer(guess, follower_count_A, follower_count_B)

        if is_correct is False:
            end_of_game(lose)
            break
else:
    print("No data available. Goodbye.")
