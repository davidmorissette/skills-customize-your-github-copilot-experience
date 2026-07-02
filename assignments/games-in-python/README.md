
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game using Python strings, loops, conditionals, and user input to practice game logic and control flow.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the initial game setup by choosing a target word and preparing the game state.

#### Requirements
Completed program should:
- Randomly select a word from a predefined list
- Initialize the display state with underscores for each letter
- Track guessed letters and remaining attempts

### 🛠️ Guess Handling and Display

#### Description
Accept player guesses, update the current progress display, and manage remaining attempts.

#### Requirements
Completed program should:
- Prompt the player to guess a single letter
- Reveal correctly guessed letters in the word display
- Keep incorrect guesses from counting against the player more than once
- Show the current word progress in `_ _ _` format after each guess

### 🛠️ End Conditions and Messages

#### Description
Finish the game when the player wins or loses and display the appropriate result.

#### Requirements
Completed program should:
- End when the word is fully guessed or the player runs out of allowed attempts
- Display a clear win message when the player guesses the word
- Display a lose message and reveal the target word when attempts are exhausted
