
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.array = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.max_size
        self.array[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.array[self.front]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.array[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
