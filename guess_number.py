import random

number = random.randint(1, 200)
guess = int(input("Твоё число: "))

while guess != number:
    if guess > number:
        print("Загаданное число меньше.")
    elif guess < number:
        print("Загаданное число больше.")

    guess = int(input("Твоё число: "))
