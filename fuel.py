
while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x > y or y == 0 or x < 0:
            continue

        percentage = round(x / y * 100)

        if percentage >= 99:
            print("F")
        elif percentage <= 1:
            print("E")
        else:
            print(f"{percentage}%")
        break
    except ValueError:
        pass
