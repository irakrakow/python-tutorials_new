def count_values(arr):
    # Create a dictionary with default values of 0
    count = {}

    # Iterate through the array and count the number of occurrences of each value
    for value in arr:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1

    # Print the number and the number of occurrences for each value, sorted by the key (number)
    for value in sorted(count):
        print(f"{value}: {count[value]}")


# Test the function
count_values([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
# Should print:
# 0: 4
# 1: 2
# 2: 1
# 3: 1
# 4: 3
# 5: 2
# 9: 1
