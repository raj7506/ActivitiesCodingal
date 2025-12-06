start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

all_squares = []
even_squares = []
odd_squares = []

for number in range(start, end + 1):
    square = number * number
    all_squares.append(square)

    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("All squares:", all_squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)