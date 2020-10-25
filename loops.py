dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
  print(breed)

board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
  print(game) 

for sport in sport_games:
  print(sport)

promise = "I will not chew gum in class"

for i in range(5):
  print(promise)

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print('They have the dog I want!')
    break

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  students_in_poetry.append(all_students.pop())

print(students_in_poetry)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for sale in location:
    scoops_sold += sale

print(scoops_sold)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [element for element in heights if element > 161]

print(can_ride_coaster)

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [num * 9/5 + 32 for num in celsius]

print(fahrenheit)

single_digits = list(range(10))

squares = []

for digit in single_digits:
  print(digit)
  squares.append(digit ** 2)

print(squares)

cubes = [digit ** 3 for digit in single_digits]

print(cubes)