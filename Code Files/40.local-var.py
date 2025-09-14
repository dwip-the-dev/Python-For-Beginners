def greet(name):
    local_greeting = f"Hello, {name}!" # local_greeting is a local variable
    print(local_greeting)

greet("Alice")
# print(local_greeting) # This would raise a NameError, as local_greeting is not defined in this scope