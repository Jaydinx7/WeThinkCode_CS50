vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
input = input("Input: ")

for vowel in vowels:
    if vowel in input:
        input = input.replace(vowel, "")

print(f"Output: {input}")
