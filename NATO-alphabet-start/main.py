import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

while True:
    try:
        word = input("Enter a word: ").upper()
        word_in_nato = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(word_in_nato)
        break
