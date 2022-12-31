def count_values(arr):
    # Create a dictionary with default values of 0
    count = {}
    
    # Iterate through the array and count the number of occurrences of each value
    for value in arr:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1
    
    # Create a new array with the counts in the same order as the sorted keys (numbers)
    result = [count[value] for value in sorted(count)]
    
    # Print the number and the number of occurrences for each value, sorted by the key (number)
    for value, count in sorted(count.items()):
        print(f"{value}: {count}")
        
    return result

# Test the function
print(count_values([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]))  # should print [4, 2, 1, 1, 3, 2, 0, 0, 0, 1]
# Should also print:
# 0: 4
# 1: 2
# 2: 1
# 3: 1
# 4: 3
# 5: 2
# 9: 1
