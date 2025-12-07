test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test dictionary:", test_dict)
frequency = input("Enter the value you want to check the frequency of: ")
user = int(frequency)

num = 0
for value in test_dict.values():
    if value == user:
        num += 1

print(f"The frequency of the value {user} is: {num}")