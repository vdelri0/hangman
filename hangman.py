import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6

# Create blanks
display = []
for _ in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = guess

    # Guess is not a letter in chosen_word
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You Lose T_T")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
