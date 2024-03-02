def find_maximum(numbers, compare):
    # Initialize maximum with the first element of the list
    maximum = numbers[0]
    
    # Iterate over the list starting from the second element
    for num in numbers[1:]:
        # Use the lambda function to compare and update the maximum
        maximum = compare(maximum, num)
    
    return maximum

# Example usage:
numbers = [12, 35, 67, 4, 89, 23]
max_number = find_maximum(numbers, lambda x, y: x if x > y else y)
print("Maximum number:", max_number)