# create new list from existing list
names = ["Mariya", "Batman", "spongebob"]
new_names = []

for n in names:
    if n.islower():
        n = n.capitalize()
    else:
        n = "Relax " + n.capitalize()
    new_names.append(n)

names = new_names
print(names)
print(new_names)
