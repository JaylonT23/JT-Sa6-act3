# List of strings
strings = ["apple", "banana", "kiwi", "orange", "pear", "fig", "grape"]

# Sort the list based on length and then alphabetically
sorted_strings = sorted(strings, key=lambda x: (len(x), x))

# Print the sorted list
print("Sorted strings:", sorted_strings)