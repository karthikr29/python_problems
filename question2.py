# Write a program which can compute the factorial of a given numbers.The results should be printed in a
# comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

number = int(input("Enter number to find factorial: "))
print(f"Factorial of the {number} is : ", end="")
i = number
factorial = 1
while i > 0:
    factorial *= i
    i -= 1

print(factorial)

