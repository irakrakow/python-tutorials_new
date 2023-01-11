from itertools import zip_longest
L1 = [1, 2, 3, 4, 5]
L2 = ['a', 'b', 'c', 'd', 'e']

print(list(zip(L1, L2)))

# Output
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# L1 has 5 elements.  L2 has 4 elements.  Output has only 4 elements.
L1 = [1, 2, 3, 4, 5]
L2 = ['a', 'b', 'c', 'd']

zip_L1L2 = zip(L1, L2)

print(list(zip_L1L2))

# Output
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# zip() for 3 lists
fruits = ["apples", "oranges", "bananas", "melons"]
prices = [20, 10, 5, 15]
quantities = [5, 7, 3, 4]

for fruit, price, quantity in zip(fruits, prices, quantities):
    print(f"You bought {quantity} {fruit} for ${price*quantity}")

# Output
# You bought 5 apples for $100
# You bought 7 oranges for $70
# You bought 3 bananas for $15
# You bought 4 melons for $60

# substitute None for the tuples with no corresponding index when zipped
L1 = [1, 2, 3, 4, 5]
L2 = ['a', 'b', 'c', 'd']

zipL_L1L2 = zip_longest(L1, L2)

print(list(zipL_L1L2))

# Output
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, None)]

# use fillValue to fill the empty corresponding list to some other value
L1 = [1, 2, 3, 4, 5]
L2 = ['a', 'b', 'c', 'd']

zipL_L1L2 = zip_longest(L1, L2, fillvalue="Item Not Found")

print(list(zipL_L1L2))

# Output
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'Item Not Found')]
