"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730412587"

secret_string: str = "python"
user_word: str = input("What is your " + str(len(secret_string)) + "-letter guess? ") 

while len(user_word) != len(secret_string):
    user_word = input("That was not " + str(len(secret_string)) + " letters! Try again: ")
    

number_matching_indices: int = 0 
emoji: str = ""
boolean_variable: bool = False
alternate_chr_indices: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while number_matching_indices < len(secret_string):
    if secret_string[number_matching_indices] == user_word[number_matching_indices]:
        emoji += GREEN_BOX
    else:
        while boolean_variable is False and alternate_chr_indices < len(secret_string):
            if secret_string[alternate_chr_indices] == user_word[number_matching_indices]:
                boolean_variable = True
                emoji += YELLOW_BOX
            alternate_chr_indices += 1 
        if boolean_variable is False:
            emoji += WHITE_BOX
        boolean_variable = False
        alternate_chr_indices = 0
    number_matching_indices += 1
print(emoji)
    
if user_word != secret_string: 
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")