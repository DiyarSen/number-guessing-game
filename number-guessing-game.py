import random

number_guess = random.randint(0,100)
right_entry = 10

while right_entry > 0:
    guess = int(input("Tahmininiz: "))

    if guess <= 0:
        print("Pozitif bir sayı giriniz")
        continue

    right_entry -= 1

    if number_guess == guess:
        print("Doğru tahmin, tebrikler :)")
        break

    elif number_guess > guess:
        print(f"YUKARI! Kalan hakkınız: {right_entry}")

    else :
        print(f"AŞAĞI! Kalan hakkınız: {right_entry}")

    if right_entry == 0 :
        print (f"Tahmin hakkınız kalmadı. Doğru sayı: {number_guess}")