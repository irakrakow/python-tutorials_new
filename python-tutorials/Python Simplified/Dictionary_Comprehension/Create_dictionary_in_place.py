my_dict = {
    "Spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wo": "nurse"
}

# append "man" with key to make dictionary consistent
my_dict = {key + "man": val for (key, val) in my_dict.items()}
print(my_dict)

# need items method this produces value error (too many values to unpack)
#my_dict = {key + "man": val for (key, val) in my_dict}
#print(my_dict)
