names = []

with open("names.txt") as file:
    for line in sorted(file):
        print("hello", line.rstrip())  # default is ascending order

# print names in reverse order
for name in sorted(names, reverse=True):
    print(f"hello, {name}")
