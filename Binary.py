num = float(input("Enter a decimal number: "))
binary = ""
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    for i in range(1):
        num = num // 2      
print("Binary number is:", binary)