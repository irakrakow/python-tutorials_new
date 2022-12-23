def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)

say_hello()

# Output:

#Something is happening before the function is called.
#Hello!
#Something is happening after the function is called.

#In this example, the my_decorator function is the decorator. It takes the say_hello function as an argument and returns a modified version of it that includes the additional behavior defined in the wrapper function. The say_hello function is then replaced with the modified version.

#Decorators are often used to add logging, authentication, or other types of common behavior to functions. They can also be used to add or modify the behavior of class methods.

#It's important to note that the syntax for using decorators in Python involves the use of the @ symbol, which is placed before the name of the decorator function. For example:

# @my_decorator
# def say_hello():
#   print("Hello!")
#
# This is equivalent to calling the decorator function and assigning the returned value to say_hello, as in the previous example.

# I hope this helps! Let me know if you have any questions or need further clarification on decorators in Python