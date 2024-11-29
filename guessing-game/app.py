import sys
import json
import time
import random


def game():
    print("""
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
        
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    """)

    difficulty_level = input("Enter your choice: ")

    difficulty_name_map = {"1": "Easy", "2": "Medium", "3": "Hard"}
    difficulty_count_map = {"1": 10, "2": 5, "3": 3}

    if not difficulty_level in difficulty_name_map.keys():
        print("Invalid difficulty selected! Exiting...")
        sys.exit(0)

    print(f"""
    Great! You have selected the {difficulty_name_map[difficulty_level]} difficulty level.
    Let's start the game!
        """)

    random_number = random.randint(1,100)

    total_guesses = 0

    while total_guesses < difficulty_count_map[difficulty_level]:
        start_time = time.time()
        guess = int(input("Enter your guess: "))

        total_guesses += 1

        if guess == random_number:
            print(f"Congratulations! You guessed the correct number in {total_guesses} attempts.")
            print(f"You took {round(time.time() - start_time, 2)} seconds to guess the correct number!")

            try:
                with open("./high_scores.json", 'r') as read_score:
                    high_score_data = json.loads(read_score.read())
            except:
                high_score_data = {"1": 10, "2": 5, "3": 3}
                with open("./high_scores.json", 'w') as write_file:
                    json.dump(high_score_data, write_file, indent=4)
            
            if high_score_data[difficulty_level] > total_guesses:
                high_score_data[difficulty_level] = total_guesses
                print(f"New high score in the difficulty level! You guessed the number in only {total_guesses} tries!")

            with open("./high_scores.json", 'w') as write_file:
                json.dump(high_score_data, write_file, indent=4)

            break
        elif guess > random_number:
            print(f"Incorrect! The number is less than {guess}.")
        elif guess < random_number:
            print(f"Incorrect! The number is more than {guess}.")

        if total_guesses == difficulty_count_map[difficulty_level]:
            print("Oh no you didn't guess the number in enough tries!")


while True:
    game()

    play_again = input("\n\nWant to play again? (Yes/No) ")

    if play_again.lower() == 'yes':
        game()
    else:
        sys.exit(0)