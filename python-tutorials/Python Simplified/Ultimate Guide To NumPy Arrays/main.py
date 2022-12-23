import numpy as np  # having a short abbreviation makes for cleaner code display

# create a numpy array
my_array = np.arange(8)
print(my_array)  # [0 1 2 3 4 5 6 7]   8 is the stop value
print(type(my_array))  # <class 'numpy.ndarray'>

my_array = np.arange(1, 8)
print(my_array)  # [1 2 3 4 5 6 7]   8 does not print

my_array = np.arange(1, 8, 2)  # added 3rd argument, the step value
print(my_array)  # [1 3 5 7]

my_array = np.arange(1, 8, 0.5)  # the step value is 0.5
print(my_array)  # [1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5]

# arrays from lists
# purpose:  memory efficiency
from_list = np.array([1, 2, 3])
print(from_list)  # successfully converted the list to a numpy array
print(type(from_list[0]))  # <class 'numpy.int32'>

# save memory
# might not take less time...depends on hardware and OS
from_list = np.array([1, 2, 3], dtype=np.int8)
print(from_list)  # successfully converted the list to a numpy array
print(type(from_list[0]))  # <class 'numpy.int8'>

# 2D array
from_list = np.array([[[1, 2, 3], [4, 5, 6]]], dtype=np.int8)
print(from_list)  # successfully converted the list to a numpy array
print(type(from_list[0]))  # <class 'numpy.int8'>
print(from_list)

# tuple
from_list = np.arange(0, 8, 2)
array_2d = np.array((np.arange(0, 8, 2), np.arange(1, 8, 2)))
print(from_list)  # successfully converted the list to a numpy array
print(array_2d)  # [0 2 4 6] on one row [1 3 5 7] on the second row
# tracks only the number rows and columns (21,)
print("1d shape:", my_array.shape)
# tracks the number of rows and columns (2, 4)
print("2d Shape: ", array_2d.shape)

# reshape the 2D array
array_2d = array_2d.reshape((4, 2))
print("2d Shape: ", array_2d.shape)  # (4, 2)
print("array_2d: ",array_2d)  # now 4 rows and 2 columns
