def raise_to_power(numbers, n):
    # Use map() with a lambda function to raise each number to the power of n
    powered_numbers = list(map(lambda x: x ** n, numbers))
    return powered_numbers

numbers = [1, 2, 3, 4, 5]
n = 3
powered_numbers = raise_to_power(numbers, n)
print("Numbers raised to the power of", n, ":", powered_numbers)