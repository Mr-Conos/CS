import re # import libaries
import random

phrases = ["how_is_your_day","sus","dog","i_luv_computers","i_like_code"] # list of all the phrases you can solve.
correct_phrase = random.choice(phrases) # selects a random phrase from phrases.
starting_phrase = re.sub('[a-z]', "*", correct_phrase) # replace all the letters from the phrase with "*"
print(f"Starting phrase is: {starting_phrase}. The asterisk is a letter and the _ is a space")
# defining
incorrect_guess = 0
guess_count = 0
incorrect_guesses = []
# loop
while "*" in starting_phrase:
    # users can only have 6 incorrect guesses
    user_guess = input("input a letter: ")
    if incorrect_guess >= 6:
        print("You are out of guesses :(")
        break # stops the loop
    while not (user_guess.isalpha() and len(user_guess) == 1): # makes sure the users input is only 1 character and is a letter
        user_guess = input("Please input a single letter: ").lower()
    if user_guess in correct_phrase:
        print("the letter is in the phrase")

        index_of_letter = [pos for pos, char in enumerate(correct_phrase) if char == user_guess] # gets position of the guessed letter
        for i in index_of_letter:
            starting_phrase = starting_phrase[:i] + user_guess + starting_phrase[i+1:]
        print(starting_phrase)


    else:
        print("the letter is not in the phrase")
        incorrect_guess += 1
        incorrect_guess.append(user_guess)
        
    guess_count += 1
    
else:
    print(f"You solved it! The starting phrase is {starting_phrase}. You guessed it in {guess_count} guesses.\nIncorrect Letters: {incorrect_guesses}")