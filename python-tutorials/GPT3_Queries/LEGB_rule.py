# In this code, x is a global variable, y is a local variable in the outer function, and z is a local variable in the inner function. When the inner function is executed and the line print(x, y, z) is reached, Python will first search for x in the local scope (inner), then in the enclosing scope (outer), then in the global scope, and finally in the built-in scope. It will find x in the global scope, y in the enclosing scope (outer), and z in the local scope (inner).

x = 10  # global variable


def outer():
    y = 20  # local variable in outer function - enclosing scope

    def inner():
        z = 30  # local variable in inner function - aka built-in scope
        print(x, y, z)

    inner()


outer()
