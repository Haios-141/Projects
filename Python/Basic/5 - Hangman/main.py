import random
from hangman_words import word_list
from hangman_art import logo, stages
from os import system, name


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in chosen_word:
  display.append("_")

while end_of_game == False:
  guess = input("Guess a letter in the word (if you enter more than one letter, only the first letter will be selected): ")[0].lower()

  clear()

  if guess not in display:
    #Check guessed letter
    position = 0
    
    for letter in chosen_word:
      
      if letter == guess:
        display[position] = letter
  
        #Check if user has got all letters.
        if "_" not in display:
          end_of_game = True
          print("You Win!")
    
      position += 1
  
    # Check if user is wrong.
    if guess not in chosen_word:
      # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      
      lives -= 1
      
      if lives == 0:
        end_of_game = True
        print(f"You lose. The word is: {chosen_word}")

    print(f"{' '.join(display)}")
    
  else:
    print(f"You've already guessed: {guess}")
    print(f"{' '.join(display)}")
  
  # Import the stages from hangman_art.py and make this error go away.
  print(stages[lives])