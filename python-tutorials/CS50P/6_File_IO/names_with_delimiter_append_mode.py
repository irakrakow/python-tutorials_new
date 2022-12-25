name = input("What's your name? ")

file = open("names.txt", "a")   # file handle created in write mode
file.write(f"{name}\n")         # f string makes all the difference
file.close()                    # new line added, each name on a separate line
