# Let's create your first decorator
def my_first_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Now let's use it
@my_first_decorator
def say_hello():
    print("Hello!")

# Let's call it
say_hello()