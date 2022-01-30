"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730412587"

five_character_word: str = input("Enter a 5-character word: ")

if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character = str(input("Enter a single character: "))

if len(single_character) != 1: 
    print("Error: Character must be a single character.") 
    exit()
else: 
    print("Searching for " + single_character + " in " + five_character_word) 

number_matching_indices: int = 0 

if single_character == five_character_word[0]:
    print(single_character + " found at index 0")
    number_matching_indices += 1

if single_character == five_character_word[1]:
    print(single_character + " found at index 1")
    number_matching_indices += 1

if single_character == five_character_word[2]:
    print(single_character + " found at index 2")
    number_matching_indices += 1

if single_character == five_character_word[3]:
    print(single_character + " found at index 3")
    number_matching_indices += 1

if single_character == five_character_word[4]:
    print(single_character + " found at index 4")
    number_matching_indices += 1

if number_matching_indices == 0: 
    print("No instances of " + single_character + " found in " + five_character_word)
else:
    if number_matching_indices == 1: 
        print(str(number_matching_indices) + " instance of " + single_character + " found in " + five_character_word)
    else:
        print(str(number_matching_indices) + " instances of " + single_character + " found in " + five_character_word)