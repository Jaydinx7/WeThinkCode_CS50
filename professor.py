import random


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break

    except ValueError:
        pass

lvl = random.randint(1, level)

while True:
    try:
        while True:
            guess = int(input("Guess: "))
            if guess > 0:
                break

        if guess == lvl:
            print("Just right!")
            break
        elif guess > lvl:
            print("Too large!")
        elif guess < lvl:
            print("Too small!")

    except ValueError:
        pass
