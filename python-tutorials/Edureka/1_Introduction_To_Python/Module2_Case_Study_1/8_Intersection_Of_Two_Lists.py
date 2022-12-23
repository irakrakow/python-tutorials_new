def intersect_Two_Lists(l1, l2):
    return [value for value in l1 if value in l2]


list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
print(intersect_Two_Lists(list1, list2))  # [35]
