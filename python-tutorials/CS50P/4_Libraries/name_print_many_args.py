import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# pass as many names as you want in the sys.argv array
# BUG:  prints out the program name as well as the
for arg in sys.argv:
    print("hello, my name is", arg)
print("=====================================")
print()
print("Slice the array so the argv[0] is not printed")
# fix BUG: slice the sys.argv array
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
