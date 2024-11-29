Implementation of https://roadmap.sh/projects/number-guessing-game

# Guessing Game
This is a guessing game where the user has to guess a number between 1 and 100.
The game will then tell the user if the number is higher or lower than the number the computer is thinking of.
The game ends when the user guesses the number correctly.

# How to run the game
The game can be run by executing the following command in the terminal:

```
python3 app.py 

    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
        
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    
Enter your choice: 3 

    Great! You have selected the Hard difficulty level.
    Let's start the game!
        
Enter your guess: 1
Incorrect! The number is more than 1.
Enter your guess: 5
Incorrect! The number is more than 5.
Enter your guess: 54
Incorrect! The number is more than 54.
Oh no you didn't guess the number in enough tries!


Want to play again? (Yes/No) No
```
