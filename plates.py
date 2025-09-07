def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha():
        return False

    if not (len(s) >= 2 and  len(s) <= 6):
        return False

    if not s.isalnum():
        return False

    for i, char in enumerate(s):
        if char.isdigit():
            if not s[i:].isdigit():
                return False
            if s[i] == "0":
                return False
            break

    return True


if __name__ == "__main__":
    main()
