
import random

print("🎮 Welcome to Guess the Number!")
print("I am thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a bigger number.")
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
            print(f"🎉 Correct! You won in {attempts} attempts!")
            break

    except ValueError:
        print("Please enter a valid number.")
