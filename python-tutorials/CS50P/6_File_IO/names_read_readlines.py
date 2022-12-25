with open("names.txt", "r") as file:
    lines = file.readlines()   # reads the entire file

for line in lines:
    print("hello, ", line)  #extra line between each name

for line in lines:
    print("hello", line.rstrip())  # strip out newline
