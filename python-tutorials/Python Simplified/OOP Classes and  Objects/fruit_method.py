class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.color = clr

    # details() method is related to Fruit object
    def details(self):
        print("my " + self.name + " is " + self.color)


apple = Fruit("apple", "red")
apple.details()

banana = Fruit("banana", "yellow")
banana.details()

kiwi = Fruit("kiwi", "green")
kiwi.details()
