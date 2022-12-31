import numpy as np

# Create a numpy array having NaN (Not a Number)
arr = np.array([np.nan, 1., 2., np.nan, 3., 4., 5.])

# Use the isnan function to identify the elements which are NaN
mask = np.isnan(arr)

# Use boolean indexing to filter out the NaN elements
filtered_arr = arr[~mask]
print(filtered_arr)
