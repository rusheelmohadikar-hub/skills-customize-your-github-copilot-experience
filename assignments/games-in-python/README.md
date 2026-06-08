# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman-style game in Python to practice string handling, control flow, loops, and user interaction.

## 📝 Tasks

### 🛠️ Build the Hangman game

#### Description
Write a Python program that selects a secret word from a list and allows a player to guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list
- Display the current word progress using placeholders like `_ _ _ _`
- Accept single-letter guesses and update the progress with correct letters
- Track and display the number of incorrect guesses remaining
- End the game when the player guesses the word or uses all attempts
- Show a win message or a lose message that includes the correct word

Example output:

```text
Word: _ A _ _ _
Guess a letter: A
Good guess! Current word: _ A _ _ _
```

### 🛠️ Add player feedback and replay support

#### Description
Improve the game by giving clear feedback on guesses and letting the player choose to play again.

#### Requirements
Completed program should:

- Show which letters have already been guessed
- Inform the player when a letter is not in the word or has already been guessed
- Ask the player whether they want to play again after a round ends
- Reset the game state for a new round when the player chooses to continue
