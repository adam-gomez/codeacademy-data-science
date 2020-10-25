nums = [4, 8, 15, 16, 23, 42]

double_nums = [num * 2 for num in nums]

nums = range(11)

squares = [x ** 2 for x in nums]

nums = [4, 8, 15, 16, 23, 42]

add_ten = [x + 10 for x in nums]

nums = [4, 8, 15, 16, 23, 42]

divide_by_two = [num / 2 for num in nums]

nums = [4, 8, 15, 16, 23, 42]

parity = [num % 2 for num in nums]

names = ["Elaine", "George", "Jerry", "Cosmo"]

greetings = ["Hello, " + name for name in names]

names = ["Elaine", "George", "Jerry", "Cosmo"]

first_character = [name[0] for name in names]

names = ["Elaine", "George", "Jerry", "Cosmo"]

lengths = [len(name) for name in names]

booleans = [True, False, True]

opposite = [not x for x in booleans]

names = ["Elaine", "George", "Jerry", "Cosmo"]

is_Jerry = [x == "Jerry" for x in names]

nums = [5, -10, 40, 20, 0]

greater_than_two = [x > 2 for x in nums]

nested_lists = [[4, 8], [15, 16], [23, 42]]

product = [x1 * x2 for (x1, x2) in nested_lists]

nested_lists = [[4, 8], [16, 15], [23, 42]]

greater_than = [x1 > x2 for (x1, x2) in nested_lists]

nested_lists = [[4, 8], [16, 15], [23, 42]]

first_only = [x1 for (x1, x2) in nested_lists]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

sums = [x1 + x2 for (x1, x2) in zip(a, b)]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

quotients = [num2 / num1 for (num1, num2) in zip(a, b)]

capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]

locations = [capital + ", " + country for (capital, country) in zip(capitals, countries)]

names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]

users = ['Name: ' + str(name) + ", Age: " + str(age) for (name, age) in zip(names, ages)]

a = [30, 42, 10]
b = [15, 16, 17]

greater_than = [num1 > num2 for (num1, num2) in zip(a, b)]