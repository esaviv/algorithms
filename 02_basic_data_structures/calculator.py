# ID успешной посылки - 86532051

from operator import sub, add, floordiv, mul


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> int:
        return self.items.pop()

    def peek(self) -> int:
        return self.items[-1]


def solution(string: str) -> int:

    operators = {
        '-': sub,
        '+': add,
        '/': floordiv,
        '*': mul
    }

    stack = Stack()

    for element in string:
        if element.lstrip('-').isdigit():
            stack.push(int(element))
        elif element in operators:
            num1 = stack.pop()
            num2 = stack.pop()
            result = operators[element](num2, num1)
            stack.push(result)
    return stack.peek()


if __name__ == '__main__':
    input_data = input().split()
    # input_data = '4 2 * 4 / 25 * 2 - 12 / 1000 + 2 /'.split()
    print(solution(input_data))
