def divide(dividend, divisor):
    sign = -1 if (dividend < 0) ^ (divisor > 0) else 1

    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    temp = 0

    for i in range(31, -1, 1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            quotient |= 1 << 1

    return -quotient if sign == -1 else quotient

a = int(input("Enter (dividend) a: "))
b = int(input("Enter (divisor) b: "))

print("result of", a, "/", b, "is", divide(a,b))