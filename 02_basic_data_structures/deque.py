class Deque():
    def __init__(self, n) -> None:
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size != self.max_n:
            self.queue[self.head] = value
            self.head = (self.head - 1) % self.max_n
            self.size += 1

    def push_front(self, value):
        """Готовая функция."""
        if self.size != self.max_n:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def pop_front(self):
        if self.is_empty():
            return None
        print(self.tail)
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        print(x)

    def pop_back(self):
        """Готовая функция."""
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        print(x)

# q = Deque(4)
# q.push_front(861)
# q.push_front(-819)
# print(q.queue)
# q.pop_back()
# q.pop_back()


q = Deque(7)
q.push_front(-855)
q.push_front(0)
q.pop_back()
q.pop_back()
q.push_back(844)
print(q.queue)
q.pop_back()
q.push_back(823)
print(q.queue)

# q = Deque(6)
# q.push_front(-201)
# q.push_back(959)
# q.push_back(102)
# q.push_front(20)
# print(q.queue)
# q.pop_front()
# q.pop_back()
# print(q.queue)

# q = Deque(8)
# q.push_back(1)
# q.push_back(-1)
# q.push_back(0)
# q.push_back(11)
# assert q.queue == [1, -1, 0, 11, None, None, None, None]
# q.pop_front()
# assert q.queue == [None, -1, 0, 11, None, None, None, None]


# q = Deque(8)
# q.push_front(1)
# q.push_front(-1)
# q.push_front(0)
# q.push_front(11)
# assert q.queue == [None, None, None, None, 11, 0, -1, 1]
# q.pop_back()
# assert q.queue == [None, None, None, None, 11, 0, -1, None]

# q = Deque(5)
# q.push_front(1)
# q.push_front(2)
# q.push_front(3)
# print(q.queue)
# q.push_back(1)
# q.push_back(2)
# q.push_back(3)
# print(q.queue)
# q.pop_front()
# q.pop_front()
# print(q.queue)
# q.pop_back()
# q.pop_back()
# print(q.queue)
