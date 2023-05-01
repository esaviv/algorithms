def get_num_day():
    pass


input_data = """6
1 2 4 4 6 8
3"""

data = input_data.split()
count_days = int(data[0])
income = [int(i) for i in data[1].split()]
price = int(data[3])

assert count_days == 6
assert income == [1, 2, 4, 4, 6, 8]
assert price == 3
