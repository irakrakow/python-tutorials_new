import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# pass as many names as you want in the sys.argv array
# BUG:  prints out the program name as well as the

print("-1 as the ending index chops off the last arg element when printed")
# fix BUG: slice the sys.argv array
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)
