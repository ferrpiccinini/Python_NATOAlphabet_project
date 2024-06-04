import pandas
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {key[0]:key["code"] for (index, key) in alphabet.iterrows()}
def refactor():
    choice = input("Enter a word:").upper()
    try:
        result = [print(alphabet_dict[key], end=" ") for key in choice]
    except KeyError:
        print("sorry, only letters in the alphabet please.")
        refactor()
refactor()
