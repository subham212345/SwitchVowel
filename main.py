vowels = ["a", "e", "i", "o", "u"]
phrase = input("Enter the phrase: ")
new_str = ""
for letter in phrase:
    letter_lower = letter.lower()
    if letter_lower in vowels:

        if letter_lower != "u":
            index_letter = vowels.index(letter_lower)
            if letter.isupper():
                new_str += vowels[index_letter + 1].upper()
            else:
                new_str += vowels[index_letter + 1]
        elif letter_lower == "u":
            if letter.isupper():
                new_str += "a".upper()
            else:
                new_str += "a"
    else:
        if letter.isupper():
            new_str += letter.upper()
        else:
            new_str += letter

print(f"The new phrase is: {new_str}")