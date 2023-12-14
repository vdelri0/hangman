import os
import random
from hangman_art import stages, logo
from hangman_words import word_list

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

end_of_game = False
chosen_word = random.choice(word_list)

lives = 6
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(len(chosen_word)):
    display.append("_")

guessed_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    cls()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}.")
    else:
        guessed_letters.append(guess)

        # Check guessed letter
        for i, letter in enumerate(chosen_word):
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[i] = guess

        # Guess is not a letter in chosen_word
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You Lose T_T\n")
                print(f"The right word was {chosen_word}.\n")

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])
