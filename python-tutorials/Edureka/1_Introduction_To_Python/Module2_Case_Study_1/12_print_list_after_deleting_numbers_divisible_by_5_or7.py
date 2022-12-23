numbers = [12, 24, 35, 70, 88, 120, 155]

# Create a new list using list comprehension, with only the numbers
# that are not divisible by 5 or 7
filtered_numbers = [number for number in numbers if number %
                    5 != 0 and number % 7 != 0]

# Print the filtered list
print(filtered_numbers)

# This program first defines the original list of numbers. Then, it uses list comprehension to create a new list, filtered_numbers, which contains only the numbers from the original list that are not divisible by 5 or 7. Finally, it prints the filtered list to the console.

# The key part of the program is the list comprehension expression [number for number in numbers if number % 5 != 0 and number % 7 != 0], which creates a new list with only the numbers that are not divisible by 5 or 7. The if clause at the end of the expression filters out the numbers that are divisible by 5 or 7.

# If you run this program, the output will be the list [12, 24, 88], which contains only the numbers from the original list that are not divisible by 5 or 7.
