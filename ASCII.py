word = input("Enter a word: ")
Ascii = []
for char in word:
    Ascii.append(ord(char))
print("The ASCII values of",word, "are:", Ascii)