class Customer:
    title = ""
    fname = ""
    lname = ""
    isblacklisted = 0

    def __init__(self):
        self.title = ""

    def __str__(self):
        return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname + " Blacklisted:" + self.isblacklisted

    def setIsblacklisted(self, isblacklisted):
        self.isblacklisted = isblacklisted

    def isblacklisted(self):
        return self.isblacklisted

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setFname(self, fname):
        self.fname = fname

    def getFname(self):
        return self.fname

    def setLname(self, lname):
        self.lname = lname

    def getLname(self):
        return self.lname


customer1 = Customer()
customer1.setTitle("Mr.")
customer1.setFname("Barack")
customer1.setLname("Obama")

customer2 = Customer()
customer2.setTitle("Mrs.")
customer2.setFname("George")
customer2.setLname("Bush")

# first customer
print(f"First Customer Title: {customer1.getTitle()}")
print(f"First Customer FName: {customer1.getFname()}")
print(f"First Customer LName: {customer1.getLname()}")
# second customer
print(f"Second Customer Title: {customer2.getTitle()}")
print(f"Second Customer FName: {customer2.getFname()}")
print(f"Second Customer LName: {customer2.getLname()}")
