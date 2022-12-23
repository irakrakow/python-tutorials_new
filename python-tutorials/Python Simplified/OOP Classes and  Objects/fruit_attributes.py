class Fruit:  # Fruit object, run automatically when Fruit class is created
    def __init__(self, name, color):
        self.name = name  # name attribute of this object
        self.color = color  # color attribute of this object
        


my_apple = Fruit("apple", "red")  # a red apple
my_banana = Fruit("banana", "yellow")  # a yellow banana
my_kiwi = Fruit("kiwi", "green")  # a green kiwi

print(my_apple.name)  # my_apple has the name apple
print(my_apple.color)  # my_apple has the color red

print(my_banana.name)  # my_banana has the name banana
print(my_banana.color)  # my_banana has the color yellow

print(my_kiwi.name)  # my_kiwi has the name kiwi
print(my_kiwi.color)  # my_kiwi has the color green
