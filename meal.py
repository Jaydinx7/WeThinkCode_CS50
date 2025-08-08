def main():
    x = convert(input("What time is it? ").strip())
    if x <= 8 and x >= 7:
        print("breakfast time")
    elif x >= 12 and x <= 13:
        print("lunch time")
    elif x >= 18 and x <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
