class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

class MyStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)
        for _ in range(self.queue.size() - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self) -> int:
        return self.queue.dequeue()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.is_empty()
