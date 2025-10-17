num = int(input("Enter the base number: "))
power = int(input("Enter the power: "))

# Anything to the power 0 is 1
result = 1

for i in range(power):
    result = result * num

print(num, "to the power", power, "is", result)