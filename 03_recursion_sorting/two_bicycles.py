def get_num_day(income):
    pass


input_data = """6
1 2 4 4 6 8
3"""

data = input_data.split('\n')
count_days = int(data[0])
incomes = [int(i) for i in data[1].split()]
price = int(data[2])


assert count_days == 6
assert incomes == [1, 2, 4, 4, 6, 8]
assert price == 3
