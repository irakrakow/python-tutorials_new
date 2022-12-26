class Guitar:
    def __init__(self) -> None:
        self.n_strings = 6
        self.play()  # called inside class

    def play(self):
        # play() invokes a function
        # object.play() invokes a method in the object
        print("pam pam pam pam pam pam pam pam")


my_guitar = Guitar()
print(my_guitar.n_strings)
my_guitar.play()
