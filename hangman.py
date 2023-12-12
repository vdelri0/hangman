import random

display = []
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}\n")

for _ in range(len(chosen_word)):
    display.append("_")

guess = input("Guess a letter: ").lower()


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for i, letter in enumerate(chosen_word):
    if letter == guess:
        display[i] = guess

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)