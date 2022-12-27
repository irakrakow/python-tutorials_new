with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# more readable
print("=================================================")
students = []  # empty list to start
print("split csv file into name, house")
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")  # append to list

for student in sorted(students):  # sorted by each line
    print(student)
