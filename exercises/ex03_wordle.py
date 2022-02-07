"""Exercise 3 Structured Wordle!"""


__author__ = "730412587"


def contains_char(str1_par_search: str, str2_single_char: str) -> bool:  # parameters aka the guess word and single char
    """Contains_char Function to test if 1st parameter string is equal to 2nd parameter of single letter guess."""
    assert len(str2_single_char) == 1
    number_matching_indices: int = 0
    while number_matching_indices < len(str1_par_search):  # if the single char is found at any index of the first guess string
        if str1_par_search[number_matching_indices] == str2_single_char:
            return True
        number_matching_indices += 1  # incrementation at same line at if statement but within loop, otherwise false
    return False

def emojified(str1_guess: str, str2_secret: str) -> str:
    """Emojified function to assign colored emoji boxes to index matches for string guesses."""
    assert len(str1_guess) == len(str2_secret)
    number_matching_indices: int = 0
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while number_matching_indices < len(str1_guess): 
        if str1_guess[number_matching_indices] == str2_secret[number_matching_indices]:
            emoji += GREEN_BOX  # no need to print emoji; it will increment greenbox if if statement applies 
        else:  
            if contains_char(str2_secret, str1_guess[number_matching_indices]) is True:
                emoji += YELLOW_BOX
            elif contains_char(str2_secret, str1_guess[number_matching_indices]) is False:  # be careful; its else & if so elif
                emoji += WHITE_BOX
        number_matching_indices += 1  # incrementation goes here 
    return emoji

def input_guess(expected_length: int) -> str:  # careful here; the parameter and return type can be different, but return type in end should be whats declared
    """Purpose is to make user input words until the user's word matches the expected length of the parameter."""
    user_guess_word: str = input(f"Enter a {expected_length} character word: ")  # use f string; no need to concatenate
    while len(user_guess_word) != expected_length:  # prompts user to eventually put in word of correct length
        user_guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return(user_guess_word)

def main() -> None:
    """The entrypoint of the program and main game loop.""" 
    target_secret_word: str = "codes"  # store variables you'll consistently need here 
    num_user_turns: int = 1  # keeps track of user turns starting at 1 not 0
    turns_variable: int = 6  # create turns variable to not hardcode
    boolean_variable: bool = True  # way to leave if statements within loop
    while num_user_turns <= turns_variable and boolean_variable: 
        print(f"=== Turn {num_user_turns}/6 ===")  # make it f-string;lights up blue
        main_user_guess = input_guess(len(target_secret_word))  # not 5 char., but len(target_wrd) since user may input any number of characters, and we'll still need to loop through 
        emojified_variable = emojified(main_user_guess, target_secret_word)  # to call function, ensure arguments inside paren. 
        print(emojified_variable)
        if main_user_guess == target_secret_word:
            print(f"You won in {num_user_turns}/6 turns!")
            boolean_variable = False  # remember to reassign boolean variable 
        if main_user_guess != target_secret_word and num_user_turns == turns_variable:
            print("X/6 - Sorry, try again tomorrow!")
        num_user_turns += 1  # put at end, must reach if statement then increment by 1

if __name__ == "__main__":
    main()