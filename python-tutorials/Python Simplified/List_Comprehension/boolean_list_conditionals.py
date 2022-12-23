# Traditional way
print("old way: ")
bits = [False, True, False, False, True, False, False, True]
new_bits = []

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

print(bits)
print(new_bits)

print("==========================================")
print("With List Comprehension: ")
super_bits = [1 if b == True else 0 for b in bits]  # just one line
print(bits)
print(super_bits)
