my_string = "HelloMyNameIsMariya"
my_string = "".join([i for i in my_string])
print(my_string)

my_string = "".join(
    [i if i.islower() else " " + i for i in my_string ])[1:]
print(my_string)
