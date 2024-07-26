# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Letter
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

# NAMES LIST
name_list = open('Input/Names/invited_names.txt').read().splitlines()
# print(name_list)

for invited_name in name_list:
    personalized_letter = letter.replace("[name]", invited_name)
    # Define the file name for each personalized letter
    file_name = f"./Output/ReadyToSend/letter_for_{invited_name}.txt"

    with open(file_name, mode="w") as completed_letter:
        completed_letter.write(personalized_letter)

    #print(personalized_letter)


C:\Users\rsharpe\Desktop\Mail Merge Project Start again\mail_main.py