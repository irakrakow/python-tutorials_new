def sort_words(words):
    # Split the input string into a list of words
    word_list = words.split(',')

    # Sort the list of words alphabetically
    word_list.sort()

    # Join the sorted list of words into a comma-separated string
    sorted_words = ','.join(word_list)

    # Return the sorted string
    return sorted_words


# Example usage
input_string = "without,hello,bag,world"
sorted_words = sort_words(input_string)
print(sorted_words)  # Output: "bag,hello,without,world"
