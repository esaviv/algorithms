# ID успешной посылки - 86649257

from operator import sub, add, floordiv, mul


class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('Стек пуст.')
        return self.items.pop()


operators = {
    '-': sub,
    '+': add,
    '/': floordiv,
    '*': mul
}


def get_result(reverse_polish_notation: str) -> int:
    stack = Stack()
    for element in reverse_polish_notation:
        if element in operators:
            num1, num2 = stack.pop(), stack.pop()
            result = operators[element](num2, num1)
            stack.push(result)
        else:
            stack.push(int(element))
    return stack.pop()


if __name__ == '__main__':
    input_data = input().split()
    print(get_result(input_data))
