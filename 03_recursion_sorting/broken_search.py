# ID успешной посылки - 87008535

from typing import List


def broken_search(array: List[int], target: int) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[left] <= array[mid]:
            if array[mid] > target >= array[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if array[mid] < target <= array[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == '__main__':
    _: int = int(input())
    search_element: int = int(input())
    array_elements: str = [int(element) for element in input().split()]

    element_index: int = broken_search(array_elements, search_element)

    print(element_index)
