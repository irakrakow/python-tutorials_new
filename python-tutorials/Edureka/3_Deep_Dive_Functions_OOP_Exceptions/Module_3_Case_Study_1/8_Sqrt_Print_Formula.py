import math

C = 50
H = 30


def calculate_Q(D):
    Q = math.sqrt((2 * C * D) / H)
    return Q


# Read input values as a comma-separated string
input_string = "100,150,180"

# Split the string into a list of integers
input_values = list(map(int, input_string.split(',')))

# Calculate and print Q for each input value
for D in input_values:
    Q = str(int(calculate_Q(D)))
    print(Q)
