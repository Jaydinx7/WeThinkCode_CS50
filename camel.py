camel_case = input("camelCase: ")
snake_case = ""

for x in camel_case:
    if x.isupper():
        snake_case += "_" + x.lower()
    else:
        snake_case += x

print(f"snake_case: {snake_case}")
