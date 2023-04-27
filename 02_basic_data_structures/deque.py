# ID успешной посылки - 86533473

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
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, value):
        if self.size != self.max_n:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        print(x)

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        print(x)


# input_data = """6
# 6
# push_front -201
# push_back 959
# push_back 102
# push_front 20
# pop_front
# pop_back"""


def solution():
    deque = Deque(max_deque_size)

    methods = {
        'push_back': deque.push_back,
        'push_front': deque.push_front,
        'pop_front': deque.pop_front,
        'pop_back': deque.pop_back
    }

    for command in commands:
        if 'push' in command:
            command, num = command.split()
            try:
                methods.get(command)(int(num))
            except OverflowError:
                print('error')
        else:
            try:
                methods.get(command)()
            except IndexError:
                print('error')


if __name__ == '__main__':
    count_command = int(input())
    max_deque_size = int(input())
    commands = [input() for _ in range(count_command)]
    # data = input_data.split('\n')
    # count_command = int(data[0])
    # max_deque_size = int(data[1])
    # commands = data[2:]
    solution()
