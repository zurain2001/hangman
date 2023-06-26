"""
Program name: Hangman
Date: 25th June 2023
Developer: Zurain Zeeshan

"""
import random
import hangman_art
from hangman_words import word_list

print(hangman_art.logo)
print("Welcome to HangMan!")
input("Press Enter to continue ... ")
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

print(display)

lives = 6

while '_' in display and lives > 0:
    guess = input("Guess a letter. ").lower()

    if guess in display:
        print("You have already guessed this letter.")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            print("You chose the correct letter.")

    if guess not in chosen_word:
        lives -= 1
        print("You chose the wrong letter.")
        print(f"Lives remaining: {lives}")

    print(display)
    from hangman_art import stages
    print(stages[lives])

if '_' in display:
    print("You lost.")
else:
    print("You won.")
    print(f"The word is: {''.join(display)}")