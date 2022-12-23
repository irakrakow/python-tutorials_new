# a list with duplicates
print("A list allows duplicates")
myList = [8, 7, 6, 6, 5, 9, 3]
print(myList)

print("=============================")
print("A set does not allow duplicates")
print("By default, the set is sorted in ascending order! ")
mySet = set(myList)
print(mySet)
myList = list(mySet)
print(myList)
print("=============================")
# can be combined...don't need list variable
print(list(set(mySet)))
print(set(list(myList)))
