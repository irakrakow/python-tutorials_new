sentence = input("Enter a sentence: ")

upper_count = 0
lower_count = 0

for c in sentence:
    if c.isupper():
        upper_count += 1
    elif c.islower():
        lower_count += 1

print(f"UPPER CASE:  {upper_count}")
print(f"LOWER CASE:  {lower_count}")
