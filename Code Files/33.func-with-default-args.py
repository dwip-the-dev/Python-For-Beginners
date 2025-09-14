def greet(name, message="Hello"):
    """
    Greets a person with a customizable message.

    Args:
        name (str): The name of the person to greet.
        message (str, optional): The greeting message. Defaults to "Hello".
    """
    print(f"{message}, {name}!")

# Calling the function with all arguments
greet("Alice", "Good morning")

# Calling the function using the default message
greet("Bob")

# Calling the function with a different message
greet("Charlie", "Hi there")