import random

bases = ["A", "T", "C", "G"]
strand1 = random.choices(bases, k=10)
print(strand1)

# this is a dictionary of lists
dna = {
    key:
    [val, ("T" if val == "A"
           else "A" if val == "T"
           else "C" if val == "G"
           else "G")]
    for (key, val) in enumerate(strand1)
}

print(dna)
