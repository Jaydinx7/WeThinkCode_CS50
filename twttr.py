vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
twttr = input("Input: ")

for vowel in vowels:
    if vowel in twttr:
        twttr = twttr.replace(vowel, "")

print(f"Output: {twttr}")
