# ID успешной посылки - 86611401

class EmptyException(IndexError):
    pass


class FullException(IndexError):
    pass


class Deque:
    def __init__(self, max_deque_size) -> None:
        self.elements = [None] * max_deque_size
        self.max_size = max_deque_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.max_size

    def get_index(self, attribute, is_sum):
        if is_sum:
            return (attribute + 1) % self.max_size
        else:
            return (attribute - 1) % self.max_size

    def push_back(self, value):
        if self.is_full():
            raise FullException(
                'В деке уже находится максимальное число элементов.'
            )
        self.elements[self.tail] = value
        self.tail = self.get_index(self.tail, True)
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            raise FullException(
                'В деке уже находится максимальное число элементов.'
            )
        self.elements[self.head - 1] = value
        self.head = self.get_index(self.head, False)
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise EmptyException('Дек пуст.')
        pop_element = self.elements[self.head]
        self.head = self.get_index(self.head, True)
        self.size -= 1
        return pop_element

    def pop_back(self):
        if self.is_empty():
            raise EmptyException('Дек пуст.')
        pop_element = self.elements[self.tail - 1]
        self.tail = self.get_index(self.tail, False)
        self.size -= 1
        return pop_element


def get_result():
    deque = Deque(max_deque_size)
    result = []
    for command in commands:
        command, *num = command.split()
        try:
            value = getattr(deque, command)(*num)
        except FullException:
            result.append('error')
        except EmptyException:
            result.append('error')
        else:
            if value:
                result.append(value)
    return result


if __name__ == '__main__':
    count_command = int(input())
    max_deque_size = int(input())
    commands = [input() for _ in range(count_command)]
    print('\n'.join(get_result()))
