#TODO: Create a letter using starting_letter.txt 
#*for each name in invited_names.txt
#*Replace the [name] placeholder with the actual name.
#*Save the letters in the folder "ReadyToSend".
    
#*Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #*Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #*Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as files_of_names:
    person = files_of_names.readlines()

#* Loop for getting each name in the list
for name in person:
    # * Automate the file naming or writing the txt files
    name = name.replace("\n", "")
    new_text_file = "letter_for_" + name + ".txt"

    with open("./Input/Letters/starting_letter.txt", mode="r") as reading_starting_letter:
        letter = reading_starting_letter.read().replace("[name]", name)
    with open(f"./Output/ReadyToSend/{new_text_file}", mode="w") as writing_letters_file:
        writing_letters_file.write(letter)
        