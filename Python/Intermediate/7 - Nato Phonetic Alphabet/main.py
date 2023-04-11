import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

nato_alpha_list = None
while True:
    try:
        word = input("Enter a word: ").upper()
        nato_alpha_list = [nato_phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print("Enter only characters found in the Alphabet.")
        continue
    else:
        break

print(nato_alpha_list)
