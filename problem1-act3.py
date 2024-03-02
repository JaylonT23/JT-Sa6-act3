sum_of_digits = lambda num: sum(int(digit) for digit in str(num) if digit.isdigit())

# Get user input for the number
num = int(input("Enter a number: "))

# Compute the sum of digits using the lambda function
result = sum_of_digits(num)

# Print the result
print("Sum of digits:", result)