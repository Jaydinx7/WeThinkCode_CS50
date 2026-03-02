greeting = input("Greeting: ").strip().lower().capitalize()

if "Hello" in greeting:
    print("$0")
elif "H" in greeting:
    print("$20")
else:
    print("$100")
