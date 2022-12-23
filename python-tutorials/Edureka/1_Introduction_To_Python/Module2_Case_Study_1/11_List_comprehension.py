my_list = [12, 24, 35, 70, 88, 120, 155]

# remove elements at 0th, 4th, and 5th index
result = [value for i, value in enumerate(my_list) if i not in (0, 4, 5)]

# print the result
print(result)  # [24, 35, 70, 155]
