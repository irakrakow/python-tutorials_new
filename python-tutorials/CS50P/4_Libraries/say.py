import cowsay
import sys

if len(sys.argv) == 2:
    # cowsay.cow("Hello, " + sys.argv[1])  # cow says hello
    cowsay.trex("Hello, " + sys.argv[1])  # T-rex says hello instead
