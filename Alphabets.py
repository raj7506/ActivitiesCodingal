print("Welcome to the Characters! We will see if whatever Charecter you write is a number or a letter")
Character = input("Enter the character:")
#is.alpha is a way to identity if a character is a letter, and is.digit is a way to identify if the character is a number
if Character.isalpha():
    print("This is a letter")
elif Character.isdigit():
    print("This is a number")
else:
    print("This is not number or a letter")