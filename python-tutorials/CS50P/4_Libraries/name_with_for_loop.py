import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# iterate over argv to get the names
for name in sys.argv:
    print("hello, my name is", name)
