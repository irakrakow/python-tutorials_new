import random
my_list = [random.randint(1, 1000) for i in range(1001)]
divisible_by_5_and_7 = [x for x in my_list if x % 5 == 0 and x % 7 == 0]

# print the first 5 elements slicing the list
print(divisible_by_5_and_7[0:5])
