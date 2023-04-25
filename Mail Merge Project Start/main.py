with open("./Input/Names/invited_names.txt", mode="r") as files_of_names:
    person = files_of_names.readlines()

#* Loop for getting each name in the list
for name in person:
    # * Automate the file naming or writing the txt files
    name = name.strip()
    new_text_file = "letter_for_" + name + ".txt"

    with open("./Input/Letters/starting_letter.txt", mode="r") as reading_starting_letter:
        letter = reading_starting_letter.read().replace("[name]", name)
    with open(f"./Output/ReadyToSend/{new_text_file}", mode="w") as writing_letters_file:
        writing_letters_file.write(letter)
