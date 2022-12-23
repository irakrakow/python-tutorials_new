class Fruit:

    def __init__(self, name, clr):
        self.name = name
        self.color = clr
        exp_date = "07.21.2021"  # local variable to __init__, inaccessable from details()
        self.exp_date = "07.20.2021"  # OK because scope extends to all methods in Fruit class

    def details(self):
        # print("expires on " + exp_date) #produces NameError because exp_date is local variable
        # OK because self.exp_date is accessible
        exp_date = "07.22.2021"  # exp_date is local to details()
        print("expires on " + self.exp_date)
        print("expires on " + exp_date)  


apple = Fruit("apple", "red")
apple.details()
