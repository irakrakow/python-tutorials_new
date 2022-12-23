def check_divisible_by_5(binary_number):
    # Convert the binary number to an integer
    number = int(binary_number, 2)

    # Check if the number is divisible by 5
    if number % 5 == 0:
        return True
    else:
        return False


# Read the input from the user
input_string = input("Enter a sequence of separated 4 digit binary numbers: ")

# Split the input string into a list of binary numbers using the comma as the delimiter
binary_numbers = input_string.split(",")

# Keep track of the numbers that are divisible by 5
divisible_by_5 = []

# Iterate over the binary numbers
for binary_number in binary_numbers:
    # Check if the number is divisible by 5
    if check_divisible_by_5(binary_number):
        # If it is, add it to the list of divisible numbers
        divisible_by_5.append(binary_number)

# Print the list of numbers divisible by 5, separated by commas
print(", ".join(divisible_by_5))
