grocerys = {}

try:
    while True:
        item = input().strip().lower()
        if item:
            grocerys[item] = grocerys.get(item, 0) + 1

except EOFError:
    pass

for grocery in sorted(grocerys):
    print(f"{grocerys[grocery]} {grocery.upper()}")
