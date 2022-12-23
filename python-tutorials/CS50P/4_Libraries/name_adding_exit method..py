import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many argumets")

# argument checking done, print 2nd argument (argv[1])
# program has exited, should print the name
print("hello, my name is", sys.argv[1])
