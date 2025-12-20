print("List 1:")
num = int(input("Enter a number: "))
odd_numbers = [i for i in range(num) if i % 2 != 0]
even_numbers = [i for i in range(num) if i % 2 == 0]
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

print("\nList 2:")
fruits = ["apple", "banana", "mango", "orange", "grapes"]
updated_fruits = [fruit.capitalize() for fruit in fruits]
print("Original fruits list:", fruits)
print("Updated fruits list:", updated_fruits)