lines = []
while True:
    line = input("Enter a line of text: ")
    if line:
        lines.append(line.upper())
    else:
        break

for line in lines:
    print(line)
