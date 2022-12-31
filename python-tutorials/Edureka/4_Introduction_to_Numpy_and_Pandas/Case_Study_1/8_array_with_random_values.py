# Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

# Create a 10x10 array with random values
array = np.random.randint(0, 100, size=(10, 10))
print(array)

# Find the minimum and maximum values
min_value = array.min()
max_value = array.max()

print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
