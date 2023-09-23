a = input("Enter a letter: ")

vowels = ["a", "e", "i", "o", "u"]

is_vowel = False

for i in vowels:
    if a == i:
        is_vowel = True
        break  # If a match is found, set the flag to True and exit the loop

if is_vowel:
    print("It is a vowel.")
else:
    print("It's not a vowel.")
