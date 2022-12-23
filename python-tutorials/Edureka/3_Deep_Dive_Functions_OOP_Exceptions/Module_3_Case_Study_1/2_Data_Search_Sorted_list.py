def search_list(data, search_term):
    # Find the length of the data list
    n = len(data)

    # Set the start and end indices for the search
    start = 0
    end = n - 1

    # Initialize a flag to indicate if the search term was found
    found = False

    # Binary search loop
    while start <= end and not found:
        # Calculate the midpoint of the list
        mid = (start + end) // 2

        # Check if the search term is at the midpoint
        if data[mid] == search_term:
            found = True
        # Check if the search term is less than the midpoint value
        elif search_term < data[mid]:
            end = mid - 1
        # If none of the above conditions are met, the search term must be greater than the midpoint value
        else:
            start = mid + 1

    # Return the result of the search
    if found:
        return "Data found at index {}".format(mid)
    else:
        return "Data not found"


# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_term = 7
result = search_list(data, search_term)
print(result)  # Output: "Data found at index 6"
