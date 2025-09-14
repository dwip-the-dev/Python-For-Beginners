class Stack:
    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def is_empty(self):
        """Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """Adds an item to the top of the stack.

        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the item from the top of the stack.

        Returns:
            Any: The item removed from the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """Returns the item at the top of the stack without removing it.

        Returns:
            Any: The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack")
        return self.items[-1]

    def size(self):
        """Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)

# Example Usage:
if __name__ == "__main__":
    my_stack = Stack()

    print(f"Is stack empty? {my_stack.is_empty()}")  # Output: True

    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print(f"Stack size: {my_stack.size()}")  # Output: 3
    print(f"Top element: {my_stack.peek()}")  # Output: 30

    popped_item = my_stack.pop()
    print(f"Popped item: {popped_item}")  # Output: 30
    print(f"Stack after pop: {my_stack.items}")  # Output: [10, 20]

    my_stack.pop()
    my_stack.pop()

    print(f"Is stack empty? {my_stack.is_empty()}")  # Output: True

    try:
        my_stack.pop()
    except IndexError as e:
        print(f"Error: {e}")  # Output: Error: Cannot pop from an empty stack