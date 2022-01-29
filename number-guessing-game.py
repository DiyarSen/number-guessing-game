import random

number_guess = random.randint(0,100)
right_entry = 10

print("It's between 0 - 100")

while right_entry > 0:
    guess = int(input("What is your guess? "))

    if guess <= 0:
        print("Please enter a positive number!")
        continue

    right_entry -= 1

    if number_guess == guess:
        print("Right guess, congrats :)")
        break

    elif number_guess > guess:
        print(f"UP! Your remaining right is: {right_entry}")

    else :
        print(f"DOWN! Your remaining right is: {right_entry}")

    if right_entry == 0 :
        print (f"Your rights are done. The right number is: {number_guess}")
