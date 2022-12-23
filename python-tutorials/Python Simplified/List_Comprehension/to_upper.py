fruits = ["apples", "bananas", "strawberries"]
uppercase_fruits = []

for f in fruits:
    print(f.upper())
    uppercase_fruits.append(f)
print(uppercase_fruits)  # does not uppercase

# list comprehension
print("List Comprehension: ")
fruits_list = ["apples", "bananas", "strawberries"]
fruits_list = [f.upper() for f in fruits_list]
print(fruits_list)
