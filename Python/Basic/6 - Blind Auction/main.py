from art import logo
from os import system, name


def clear():
  # for windows
  if name == "nt":
    _ = system("cls")
 
  # for mac and linux(here, os.name is 'posix')
  else:
    _ = system("clear")


def highest_bidder(bidder_list):
  highest_bid = 0
  highest_bidder = ""
  
  for info in bidder_list:
    for bidder in info:
      current_bid = info[bidder]
      
      if highest_bid < current_bid:
        highest_bid = current_bid
        highest_bidder = bidder
        
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


print(logo)
print("\nWelcome to the secret auction program.")

bids_list = []
continue_bid = True

while continue_bid:
  bidder_name = input("What's your name? ")
  price = int(input("What's your bid? $"))

  bids_list.append({
    bidder_name: price,
  })
  print(bids_list)

  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  while (more_bidders != "yes" and more_bidders != "y") and (more_bidders != "no" and more_bidders != "n"):
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

  clear()
  
  if more_bidders == "no" or more_bidders == "n":
    continue_bid = False
    highest_bidder(bids_list)