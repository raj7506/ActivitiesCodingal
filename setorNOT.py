def setorNOT(number, n):
    mask = 1 << (n - 1)

    if number & mask:
        print("SET")
    else:
        print("Not SET")

number = int(input("Enter Number: "))
n = int(input("Enter a bit position: "))

setorNOT(number, n)