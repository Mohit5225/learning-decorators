def smart_decorator(func):
    def wrapper(*args, **kwargs):  # This is the key - it accepts any arguments
        print(f"About to call {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")
        return result
    return wrapper

@smart_decorator
def add_numbers(a, b):
    return a + b

# Try it
result = add_numbers(3, 5)
print(f"Final result: {result}")