import inflect
p = inflect.engine()

names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)

except (EOFError):
    adieu = p.join(names)
    print("\nAdieu, adieu, to", adieu)
