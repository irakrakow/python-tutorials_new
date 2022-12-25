names = []

for _ in range(3):  # don't need the names variable - use placedholder instead of i or some other variable
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")
