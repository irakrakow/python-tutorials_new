name = input("What's your name? ")

file = open("names.txt", "a")  # opens in append mode
file.write(name)  # need newline delimiter
file.close()
