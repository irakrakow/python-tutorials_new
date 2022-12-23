names = ['Mariya', 'Gandalf', 'Batman']
profs = ['programmer', 'wizard', 'superhero']

my_dict = {}

for (key, value) in zip(names, profs):
    my_dict[key] = value

print(my_dict)
