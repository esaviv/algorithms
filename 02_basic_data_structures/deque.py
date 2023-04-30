# ID успешной посылки - 86649169

from typing import List


class EmptyException(Exception):
    pass


class FullException(Exception):
    pass


class Deque:
    def __init__(self, max_deque_size: int) -> None:
        self.elements = [None] * max_deque_size
        self.max_size = max_deque_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size >= self.max_size

    def get_index(self, attribute: int, is_sum: bool) -> int:
        index = (attribute + 1) % self.max_size if is_sum else (attribute - 1) % self.max_size
        return index

    def push_back(self, value: int) -> None:
        if self.is_full():
            raise FullException(
                'В деке уже находится максимальное число элементов.'
            )
        self.elements[self.tail] = value
        self.tail = self.get_index(self.tail, True)
        self.size += 1

    def push_front(self, value: int) -> None:
        if self.is_full():
            raise FullException(
                'В деке уже находится максимальное число элементов.'
            )
        self.elements[self.head - 1] = value
        self.head = self.get_index(self.head, False)
        self.size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise EmptyException('Дек пуст.')
        pop_element = self.elements[self.head]
        self.head = self.get_index(self.head, True)
        self.size -= 1
        return pop_element

    def pop_back(self) -> int:
        if self.is_empty():
            raise EmptyException('Дек пуст.')
        pop_element = self.elements[self.tail - 1]
        self.tail = self.get_index(self.tail, False)
        self.size -= 1
        return pop_element


def get_result() -> List[int]:
    deque = Deque(max_deque_size)
    result = []
    for command in commands:
        command, *num = command.split()
        try:
            value = getattr(deque, command)(*num)
        except (FullException, EmptyException):
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
