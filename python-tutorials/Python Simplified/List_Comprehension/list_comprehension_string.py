my_string = "HelloMyNameIsMarya"
my_string = [i for i in my_string]
print(my_string)  # each character is an element in a list
print("each character is a list element")

print("=====================================================")
print("each word separated by a space ")
my_string = "".join(
    [i if i.islower() else " " + i for i in my_string])[1:]
print(my_string)
