# Get the input string
input_str = input("Enter a line with duplicate words separated by spacesmy: ")

# Split the input string into a list of words
words = input_str.split()

# Remove duplicate words and sort the remaining words alphanumerically
unique_words = sorted(set(words))

# Print the resulting list of words
print(" ".join(unique_words))
