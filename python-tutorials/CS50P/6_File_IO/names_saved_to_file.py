name = input("What's your name? ")

file = open("names.txt", "w")  # file handle created in write mode
file.write(name)
file.close()  # only the last name exists
