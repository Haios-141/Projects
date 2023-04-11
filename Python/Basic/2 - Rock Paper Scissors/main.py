import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

list = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if choice >= 0 and choice <= 2:

    print(list[choice])
    print("Computer chose:")
    
    if choice == computer_choice:
        print(list[choice])
        print("It's a draw")
    elif \
    (choice == 0 and computer_choice == 2) or \
    (choice == 1 and computer_choice == 0) or \
    (choice == 2 and computer_choice == 1):
        print(list[computer_choice])
        print("YOU WIN!!! 🥳🥳🥳")
    else:
        print(list[computer_choice])
        print("You Lose 😞😞😞")
else:
    print("Invalid choice. Please restart the program and Type 0 for Rock, 1 for Paper or 2 for Scissors.")

# Rock (0) > Scissor (2)
# Scissor (2) > Paper (1)
# Paper (1) > Rock (0)