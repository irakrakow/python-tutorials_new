import numpy as np

# Create a random vector of size 30 with integers between 0 and 100
vector = np.random.randint(0, 101, 30)

# Round each number in the vector to 3 decimal places
vector = [round(num, 3) for num in vector]

# Find the mean value of the vector
mean = np.mean(vector)

# Print the vector and the mean value
print(f'Vector: [{", ".join(map(str, vector))}]')
print(f'Mean value: {mean:.3f}')