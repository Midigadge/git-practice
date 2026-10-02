import random

def play_game(bestscore=float('inf')):
    attempts = 0
    guessed = False

    print("\nNumber Guessing Game")

    minrange = int(input("Enter the minimum range: "))
    maxrange = int(input("Enter the maximum range: "))

    secret = random.randint(minrange, maxrange)

    while attempts < 7:
        guess = int(input(f"Guess the number between {minrange} and {maxrange}: "))
        attempts += 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"You are correct, It took {attempts} attempts.")
            guessed = True
            break 

    if not guessed:
        print(f"You took too many tries. The secret number was {secret}.")

    score = attempts if guessed else float('inf')

    if score < bestscore:
        bestscore = score

    if bestscore != float('inf'):
        print(f"Best score: {bestscore} attempts")
    else:
        print("Best score: None yet")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_game(bestscore)
    else:
        print("Thanks for playing!")

play_game()