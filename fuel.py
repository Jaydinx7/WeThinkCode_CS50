def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
             pass



def convert(fraction):
    try:
        x,y = fraction.split("/")

        x = int(x)
        y = int(y)

    except ValueError:
        raise ValueError

    if x > y or x < 0:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    return round(x / y * 100)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
