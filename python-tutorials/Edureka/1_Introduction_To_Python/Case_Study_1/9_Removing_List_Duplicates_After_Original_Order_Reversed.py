myList = [12, 24, 35, 88, 120, 155, 88, 120, 155]

# set cannot have duplicates, so wrapping myList inside set removes duplicates
myList_noDups = set(myList)

# convert back to list
print(list(myList_noDups))

# print(list(myList).sort())
