# Using a list as a stack

class Stack:
    def __init__(self, items=None):
        if not items:
            self.stack = []
        else:
            self.stack = items

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()

    def __str__(self):
        return str(self.stack)

def test():
    stack = Stack()
    print(f"Try to pop the stack when empty: {stack.pop()}")

    stack.push("cat")
    stack.push("dog")
    stack.push("elephant")
    print(f"Stack: {stack}")

    print(f"Pop top: {stack.pop()}")
    print(f"Stack: {stack}")
    stack.push("zebra")

    print(f"Peek at top: {stack.peek()}")
    print(f"Stack: {stack}")

    print(f"Is the stack empty? {stack.isEmpty()}")
    print(f"Size of the stack: {stack.size()}")

    stack.clear()
    print(f"Stack: {stack}")

# test()    # comment out to use Stack class with browser

