class Fruit:

    # __init__ automatically called when we initialize attributes
    # __init__  has a reserved name
    # __self__ refers to the current instance of the object
    def __init__(self, name, color):
        print(f"in __init__,  {name}  instance being created")
        self.name = name
        self.color = color


# new instance of Fruit class
my_fruit = Fruit("some name", "some color")
print("in __init__ method again, after instance has been initialized.")

my_apple = Fruit("apple", "red")  # a red apple
my_banana = Fruit("banana", "yellow")  # a yellow banana
my_kiwi = Fruit("kiwi", "green")  # a green kiwi

print(my_apple.name)  # my_apple has the name apple
print(my_apple.color)  # my_apple has the color red

print(my_banana.name)  # my_banana has the name banana
print(my_banana.color)  # my_banana has the color yellow

print(my_kiwi.name)  # my_kiwi has the name kiwi
print(my_kiwi.color)  # my_kiwi has the color green
