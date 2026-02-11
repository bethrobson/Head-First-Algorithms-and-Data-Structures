from collections import deque

class Queue:
    def __init__(self, items=None):
        if not items:
            self.queue = deque()
        else:
            self.queue = deque(items)
 
    def push(self, item): # enqueue
        self.queue.append(item)

    def pop(self): # dequeue
        if not self.isEmpty():
            return self.queue.popleft()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return None

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self): 
        return str(list(self.queue))

def test():
    line = Queue(["Gil", "Pete"])
    print(f"Line: {line}")

    line.push("Sara")
    print(f"Line: {line}")

    print(f"Popped customer: {line.pop()}") # Pete

    print(f"Who's at the front: {line.peek()}") # Gil

    print(f"Line: {line}")
    print(f"Size of remaining queue: {line.size()}") # 2, Gil and Sara

# test()
