age = input("Enter your age: ")
try:
    age = int(age)

    if age % 2 == 0:
        print("Your age",age,"is even")
    else:
        print("Your age",age,"is odd")

except:
    print("Please enter a number")