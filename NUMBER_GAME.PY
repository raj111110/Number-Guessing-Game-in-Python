import random

com = random.randint(1, 100)

while True:
    human = int(input("Enter your guess number: "))

    if human == com:
        print("Congratulations! You guessed the number correctly.")
        break

    elif human > com:
        print("Your guess is too high. Try again!")

    else:
        print("Your guess is too low. Try again!")