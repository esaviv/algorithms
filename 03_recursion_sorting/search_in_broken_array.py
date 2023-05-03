from typing import List


def get_element_index(
    array_elements: List[int], search_element: int
) -> int:
    pass


input_data = """9
5
19 21 100 101 1 4 5 7 12"""

data: List[str] = input_data.split('\n')
array_length: int = int(data[0])
search_element: int = int(data[1])
array_elements: List[int] = [int(i) for i in data[2].split()]

assert array_length == 9, array_length
assert search_element == 5
assert array_elements == [19, 21, 100, 101, 1, 4, 5, 7, 12]


get_element_index(array_elements, search_element)