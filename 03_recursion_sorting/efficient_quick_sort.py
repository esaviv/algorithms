# ID успешной посылки - 87000518

import random
from typing import List, Optional, Union


class User:
    def __init__(self, username: str, solved: str, errors: str) -> None:
        self.username = username
        self.solved = int(solved)
        self.errors = int(errors)

    def __gt__(self, other: 'User') -> bool:
        return (self.solved, other.errors, other.username) < (other.solved, self.errors , self.username)

    def __str__(self) -> str:
        return self.username


def quicksort(array: List[User], low: Optional[int]=None, high: Optional[int]=None):
    low = 0 if low is None else low
    high = len(array) - 1 if high is None else high

    if low >= high:
        return -1

    left, right = low, high
    pivot: User = array[random.randint(low, high)]

    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quicksort(array, low=low, high=right)
    quicksort(array, low=left, high=high)


if __name__ == '__main__':
    count_users: int = int(input())
    users: List[User] = [User(*input().split()) for _ in range(count_users)]

    quicksort(users)

    print(*users, sep='\n')
