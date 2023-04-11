from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_amount, cipher_direction):
  coded_text = ""

  for char in text:
    
    if char not in alphabet:
      coded_text += char
    else:
      pos = alphabet.index(char)

      if cipher_direction == "encode":
        new_pos = (pos + shift_amount) % len(alphabet)
      else:
        new_pos = (pos - shift_amount) % len(alphabet)
      
      coded_text += alphabet[new_pos]

  print(f"The {cipher_direction}d text is {coded_text}")

print(logo)

continue_loop = True

while continue_loop:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  while direction != "encode" and direction != "decode":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text=text, shift_amount=shift, cipher_direction=direction)
  
  restart = input("Type 'Yes' if you want to go again. Otherwise, type 'No'.\n").lower()
  while restart != "yes" and restart != "no":
    restart = input("Type 'Yes' if you want to go again. Otherwise, type 'No'.\n").lower()

  if restart == "no":
    continue_loop = False
    print("Goodbye")