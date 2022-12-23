import numpy as np

# initialize array elements to zeros
empty_array = np.zeros((2, 2))
print(empty_array)  # [[0. 0.] [0. 0.]]

# initialize array elements to ones
empty_array = np.ones((2, 2))
print(empty_array)  # #[[1. 1.] [1. 1.]]


# initialize array elements to random values
empty_array = np.empty((2, 2))
print(empty_array)  # #[[1. 1.] [1. 1.]]  looks like np.ones
# however, changing the shape fills array with random values
empty_array = np.empty((2, 2, 2))
print(empty_array)  # some random values ...Marya doesn't like it


# np.eye - diagonal has ones, other cells have zeroes
eye_array = np.eye(3)
print(eye_array)  # diagonal cells contain 1s. Other cells conain 0s.

# k parameter - offset filling 1s diagonal
eye_array = np.eye(3, k=-1)
print(eye_array)  # diagonal starts at row 2.

eye_array = np.eye(3, k=1)
print(eye_array)  # diagonal starts at column 2.

# use a filter to change 0s to 2s
eye_array = np.eye(3, k=1)
eye_array[eye_array == 0] = 2  # convert 0s to 2 s
print(eye_array)  # [[2. 1. 2.] [2. 2. 1.] [2. 2. 2.]]

# less than filter - convert 2s to 9s
eye_array = np.eye(3, k=1)
eye_array[eye_array == 0] = 2  # convert 0s to 2s
eye_array[eye_array < 2] = 9   # convert 1s to 9s
print(eye_array)  # [[2. 9. 2.] [2. 2. 9.] [2. 2. 2.]]

# Make all elements in row 1 equal to 3
eye_array = np.eye(3, k=1)
eye_array[eye_array == 0] = 2  # convert 0s to 2s
eye_array[eye_array < 2] = 9   # convert 1s to 9s
eye_array[0] = 3  # all elements in the first row are now 3
print(eye_array)  # [[3. 3. 3.] [2. 2. 9.] [2. 2. 2.]]

# now first two rows are selected
eye_array = np.eye(3, k=1)
eye_array[eye_array == 0] = 2  # convert 0s to 2s
eye_array[eye_array < 2] = 9   # convert 1s to 9s
eye_array[0] = 3  # all elements in the first row are now 3
eye_array[:2] = 3  # all elements in the first and second row are 3
print(eye_array)  # [[3. 3. 3.] [3. 3. 3.] [2. 2. 2.]]
