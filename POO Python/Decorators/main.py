from decorator import my_decorator, uppercase_decorator, split


# Exemple 1


@my_decorator
def my_function():
    print("Hello World!")


my_function()


# Exemple 2
@uppercase_decorator
def say_hello():
    return "Hello!"


print(say_hello())


# Exemple 3
@split
@uppercase_decorator
def example():
    return "Learning Python is fun!"


print(example())
