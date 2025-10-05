no1 = int(input("Please enter the first number: ")) 
no2 = int(input("Please enter the second number: "))
no3 = int(input("Please enter the third number: "))

a = [no1, no2, no3]

print("\nWhat you've chosen:")
for i in a:
    print(i)

# Ascending order
a.sort()
print("\nAscending:")
for i in a:
    print(i)

# Descending order
a.sort(reverse=True)
print("\nDescending:")
for i in a:
    print(i)