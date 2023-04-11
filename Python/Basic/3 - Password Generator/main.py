#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^', '@', '_']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

##------------------ USING CHOICE FUNCTION -----------------------------##
password = ""
randomised_password = ""

for i in range(0, nr_letters):
    password += random.choice(letters)

for i in range(0, nr_symbols):
    password += random.choice(symbols)

for i in range(0, nr_numbers):
    password += random.choice(numbers)

randomised_password = ''.join(random.sample(password, len(password)))

print(randomised_password)

##----------------- Without Choice Function ---------------------##

# password = ""
# randomised_password = ""
# letter_length = len(letters) - 1
# symbols_length = len(symbols) - 1
# numbers_length = len(numbers) - 1

# for i in range(0, nr_letters):
#     index = random.randint(0 , letter_length)
#     password += letters[index]

# for i in range(0, nr_symbols):
#     index = random.randint(0 , symbols_length)
#     password += symbols[index]

# for i in range(0, nr_numbers):
#     index = random.randint(0 , numbers_length)
#     password += numbers[index]

# randomised_password = ''.join(random.sample(password, len(password)))
# print(randomised_password)