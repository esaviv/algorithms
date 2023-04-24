class StackMax():
    def __init__(self) -> None:
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> str:
        if len(self.items) == 0:
            print('error')
        else:
            self.items.pop()

    def get_max(self) -> int:
        if len(self.items) == 0:
            print(None)
        else:
            print(max(self.items))


input_data = """7
get_max
pop
pop
pop
push 10
get_max
push -9"""


data = input_data.split('\n')
count = int(data[0])
commands = data[1:]

# count = int(input())
# commands = [input() for _ in range(count)]

stack = StackMax()

methods = {
    'push': stack.push,
    'pop': stack.pop,
    'get_max': stack.get_max
}


def test():
    for command in commands:
        if 'push' in command:
            command, num = command.split()
            methods.get(command)(int(num))
        else:
            methods.get(command)()


if __name__ == '__main__':
    test()
