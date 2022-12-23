# a list allows duplicates.  A set does nto allow duplicates

nums_as_list = [1, 1, 2, 3, 3, 3, 4, 4]
nums_as_set = set(nums_as_list)
print(f"nums as list: {nums_as_list}")
print(f"Number of elements:  {len(nums_as_list)}")  # 8
print(f"nums_as_set: {nums_as_set}")
print(f"Number of elements: {len(nums_as_set)}")  # 4
