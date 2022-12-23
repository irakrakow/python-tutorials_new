# initialize a dictionary to store the counts
counts = {}

# get the input string
string = input("Enter a string: ")

# iterate over each character in the string
for char in string:
  # if the character is not in the dictionary, add it with a count of 1
  if char not in counts:
    counts[char] = 1
  # if the character is already in the dictionary, increment its count by 1
  else:
    counts[char] += 1

# print the counts
for char, count in counts.items():
  print("{},{}".format(char, count))
