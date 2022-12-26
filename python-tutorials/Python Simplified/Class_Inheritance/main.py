class Guitar:
    def __init__(self) -> None:
        self.n_strings = 6

    def play(self):
        # play() invokes a function
        # object.play() invokes a method in the object
        print("pam pam pam pam pam pam pam pam")


class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__()
        self.n_strings = 8
        self.colour = ("#000000", "ffffff")
        self.cost = 50

    def playLouder(self):
        print("pam pam pam pam pam".upper())


my_guitar = ElectricGuitar()
my_guitar.playLouder()  # invoked on my_guitar instance
print("child class: ", my_guitar.n_strings)
print("parent class: ", Guitar().n_strings)
my_guitar.play()
print(my_guitar.colour)
